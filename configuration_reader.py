import configparser
class ConfigurationReader:
    """
    ConfigurationReader class is responsible for reading and extracting information from a configuration file.

    Attributes:
        config (ConfigParser): An instance of ConfigParser to handle configuration files.

    Methods:
        __init__(): Initializes an instance of the ConfigurationReader class.

        load_config_file(file_path: str) -> bool:
            Loads a configuration file from the specified path.

            Args:
                file_path (str): Path to the configuration file.

            Returns:
                bool: True if the file is successfully loaded, False otherwise.

        get_molecular_configurations() -> dict:
            Retrieves molecular configurations from the loaded configuration file.

            Returns:
                dict: A dictionary containing molecular configurations.

        get_calculation_parameters() -> dict:
            Retrieves calculation parameters from the loaded configuration file.

            Returns:
                dict: A dictionary containing calculation parameters.
    """
    def __init__(self):
        """
        Initializes an instance of the ConfigurationReader class.
        """
        self.config = configparser.ConfigParser(allow_no_value=True)
        print("configuration reader initialized.")

    def load_config_file(self, file_path: str) -> bool:
        """
        Loads a configuration file from the specified path.

        Args:
            file_path (str): Path to the configuration file.

        Returns:
            bool: True if the file is successfully loaded, False otherwise.
        """
        try:
            self.config.read(file_path)
            return True
        except configparser.Error as e:
            print(f"Error reading the config file: {e}")
            return False

    def get_molecular_configurations(self) -> dict:
        """
        Retrieves molecular configurations from the loaded configuration file.

        Returns:
            dict: A dictionary containing molecular configurations.
        """
        try:
            molecular_configs = {}
            for section_name in self.config.sections():
                if section_name.startswith('Molecule'):
                    molecular_configs[section_name] = dict(self.config.items(section_name))
            return molecular_configs
        except (configparser.Error, KeyError) as e:
            print(f"Error retrieving molecular configurations: {e}")
            return {}

    def get_calculation_parameters(self) -> dict:
        """
        Retrieves calculation parameters from the loaded configuration file.

        Returns:
            dict: A dictionary containing calculation parameters.
        """
        try:
            calculation_params = dict(self.config['CalculationParameters'])
            return calculation_params
        except (configparser.Error, KeyError) as e:
            print(f"Error retrieving calculation parameters: {e}")
            return {}
