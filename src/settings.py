import os
import importlib.util


# Get the path from the environment variable
file_path = os.getenv('DS9_SETTINGS_MODULE')

def settings():
    if file_path:
        # Ensure the file exists
        if os.path.exists(file_path):
            # Load the Python file dynamically
            spec = importlib.util.spec_from_file_location("module_name", file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            print(f"Settings loaded from {file_path}")
            return {name: value for name, value in module.__dict__.items() if not name.startswith('__')}
        else:
            print(f"Settings file not found: {file_path}")
            return {}
    else:
        raise ImportError("Settings environment variable 'DS9_SETTINGS_MODULE' not set.")
