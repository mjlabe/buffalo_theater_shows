import calendar
import json
import logging
import re
from datetime import date, datetime
from urllib.parse import urlsplit

import langchain_community.chat_models as community_chat_models
from langchain_ollama import ChatOllama

community_chat_models.ChatOllama = ChatOllama

from scrapegraphai.graphs import SmartScraperGraph


logger = logging.getLogger(__name__)


class Scraper:
    fields = ("Show", "Date(s)", "Description")
    date_range_pattern = re.compile(
        r"^\s*(?P<start_month>[A-Za-z]{3,9}\.?)\s+(?P<start_day>\d{1,2})"
        r"(?:,?\s+(?P<start_year>\d{4}))?\s*[-–—]\s*"
        r"(?:(?P<end_month>[A-Za-z]{3,9}\.?)\s+)?(?P<end_day>\d{1,2})"
        r"(?:,?\s+(?P<end_year>\d{4}))?\s*$",
        re.IGNORECASE,
    )
    single_date_pattern = re.compile(
        r"^\s*(?P<month>[A-Za-z]{3,9}\.?)\s+(?P<day>\d{1,2})"
        r"(?:,?\s+(?P<year>\d{4}))?\s*$",
        re.IGNORECASE,
    )

    def __init__(self, config):
        self.config = config

    def scrape(self, source, prompt) -> list[dict[str, str]]:
        smart_scraper_graph = SmartScraperGraph(
            prompt=prompt, source=source, config=self.config
        )
        result = smart_scraper_graph.run()
        try:
            return self.normalize_shows(result)
        except Exception as error:
            response = repr(result)
            if len(response) > 500:
                response = f"{response[:497]}..."
            logger.error(
                "Could not normalize scraper response from %s (%s): %s; response=%s",
                urlsplit(source).hostname or "unknown host",
                type(result).__name__,
                error,
                response,
            )
            raise

    @classmethod
    def normalize_shows(cls, result) -> list[dict[str, str]]:
        if isinstance(result, str):
            result = json.loads(result)
        if isinstance(result, dict):
            result = result.get("content", result)
        if isinstance(result, str):
            result = json.loads(result)
        if isinstance(result, dict):
            result = result.get("shows", result.get("events", [result]))
        if not isinstance(result, list):
            raise ValueError("Scraper response is not a list of shows")

        shows = []
        for show in result:
            if not isinstance(show, dict):
                continue
            normalized_show = {
                field: str(show.get(field) or "").strip() for field in cls.fields
            }
            normalized_show["Date(s)"] = cls.normalize_dates(normalized_show["Date(s)"])
            if normalized_show["Description"].upper() == "NA":
                normalized_show["Description"] = ""
            if normalized_show["Show"].upper() != "NA" and normalized_show["Show"]:
                shows.append(normalized_show)

        if not shows:
            raise ValueError("Scraper returned no upcoming shows")
        return shows

    @staticmethod
    def _month_number(month):
        month = month.rstrip(".").title()
        if month.casefold() == "sept":
            return 9
        for format_string in ("%B", "%b"):
            try:
                return datetime.strptime(month, format_string).month
            except ValueError:
                continue
        raise ValueError(f"Unknown month: {month}")

    @staticmethod
    def _format_date(value):
        return f"{calendar.month_abbr[value.month]} {value.day}, {value.year}"

    @classmethod
    def normalize_dates(cls, value, today=None):
        text = value.strip()
        today = today or date.today()
        match = cls.date_range_pattern.fullmatch(text)
        if match:
            try:
                start_month = cls._month_number(match["start_month"])
                end_month = cls._month_number(match["end_month"] or match["start_month"])
                start_day = int(match["start_day"])
                end_day = int(match["end_day"])
                start_year = int(match["start_year"]) if match["start_year"] else None
                end_year = int(match["end_year"]) if match["end_year"] else None
                crosses_year = end_month < start_month
                if start_year is None and end_year is None:
                    start_year = today.year
                    end_year = start_year + crosses_year
                    if date(end_year, end_month, end_day) < today:
                        start_year += 1
                        end_year += 1
                elif start_year is None:
                    start_year = end_year - crosses_year
                elif end_year is None:
                    end_year = start_year + crosses_year
                start = date(start_year, start_month, start_day)
                end = date(end_year, end_month, end_day)
            except (TypeError, ValueError):
                return text
            return f"{cls._format_date(start)} - {cls._format_date(end)}"

        match = cls.single_date_pattern.fullmatch(text)
        if match:
            try:
                month = cls._month_number(match["month"])
                day = int(match["day"])
                year = int(match["year"]) if match["year"] else today.year
                parsed = date(year, month, day)
                if not match["year"] and parsed < today:
                    parsed = date(year + 1, month, day)
            except ValueError:
                return text
            return cls._format_date(parsed)
        return text

    def aggregate(self, sources: list) -> list[list[dict[str, str]]]:
        scrape_result = []
        for source in sources:
            # Create the SmartScraperGraph instance
            scrape_result.append(
                self.scrape(
                    source=source.get("scrape_url"),
                    prompt=source.get("scrape_prompt"),
                )
            )
        return scrape_result
