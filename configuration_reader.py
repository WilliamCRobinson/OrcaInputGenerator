import configparser


class ConfigurationReader:
    # make class initiator
    def __init__(self):
        self.config = configparser.ConfigParser(allow_no_value=True)
        print("configuration reader initialized.")


    def load_config_file(self, file_path):
        try:
            self.config.read(file_path)
            return True
        except configparser.Error as e:
            print(f"Error reading the config file: {e}")
            return False

    def get_molecular_configurations(self):
        try:
            molecular_configs = {}
            for section_name in self.config.sections():
                if section_name.startswith('Molecule'):
                    molecular_configs[section_name] = dict(self.config.items(section_name))
            return molecular_configs
        except (configparser.Error, KeyError) as e:
            print(f"Error retrieving molecular configurations: {e}")
            return {}

    def get_calculation_parameters(self):
        try:
            calculation_params = dict(self.config['CalculationParameters'])
            return calculation_params
        except (configparser.Error, KeyError) as e:
            print(f"Error retrieving calculation parameters: {e}")
            return {}
