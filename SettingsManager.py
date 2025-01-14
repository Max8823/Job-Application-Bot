import yaml


class SettingsManager:
    def __init__(self, settings_file):
        self.settings_file = settings_file
        self.settings = {}

    def load_settings(self):
        try:

            with open(self.settings_file, 'r') as file:
                self.settings = yaml.safe_load(file)
            print(f"Settings loaded successfully from {self.settings_file}.")

        except FileNotFoundError:
            print(f"Settings file {self.settings_file} not found.")
            return {}

        except yaml.YAMLError as e:
            print(f"Error parsing YAML file: {e}")
            return {}

        return self.settings

    def get_setting(self, key):

        keys = key.split('.')
        current = self.settings

        for k in keys:

            if isinstance(current, dict) and k in current:
                current = current[k]

            else:
                print(f"Setting '{key}' not found.")
                return None

        return current
