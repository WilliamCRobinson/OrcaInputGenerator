import os
import configparser


def create_configuration_file():
    """
    Create a new config.ini file based on user input for calculation parameters.
    """
    config = configparser.ConfigParser()

    # Get user input for calculation parameters
    config['CalculationParameters'] = {}
    config['CalculationParameters']['header'] = input("Enter header: ")
    config['CalculationParameters']['mem'] = input("Enter memory: ")
    config['CalculationParameters']['nproc'] = input("Enter number of processors: ")


    # Get xyz files in the directory called xyzdata
    xyz_files = [file for file in os.listdir("xyzdata") if file.endswith(".xyz")]

    # Create sections for each molecule in the config file
    for i, xyz_file in enumerate(xyz_files, start=1):
        section_name = xyz_file.split(".")[0]
        config[section_name] = {}
        config[section_name]['structure_file'] = "xyzdata\\" + xyz_file
        config[section_name]['charge'] = input(f"Enter Charge for {xyz_file}: ")
        config[section_name]['spin_multiplicity'] = input(f"Enter Spin Multiplicity for {xyz_file}: ")

    save_name = input("what would you like to call your configuration file: ")
    # Save config.ini file
    with open(save_name, 'w') as config_file:
        config.write(config_file)

    print(f"{save_name} file created successfully!")

if __name__ == "__main__":
    create_configuration_file()
