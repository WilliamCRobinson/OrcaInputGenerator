"""
Main script orchestrating the workflow for generating Orca input files.

Idea: expand functionality to multiple template.orca files for different types of calcs. ie project specific templates.
        could also clean up implementation by just having one section header section.

        A handy bash script for renaming output files
        for file in *.png; do
            mv "$file" "${file%.inp}_resubx.inp"
        done


- William Robinson Jan 2024. Montana State University.
"""

from input_generator import InputGenerator
from configuration_reader import ConfigurationReader
import os


def main():
    """
    Main function orchestrating the generation of Orca input files.

    Workflow:
    1. Initialize ConfigurationReader to read molecular configurations and calculation parameters from a config.ini
       file.
    2. Load molecular configurations and calculation parameters.
    3. Initialize InputGenerator and load the template Orca input file.
    4. Iterate over molecular configurations, generate Orca input files, and save them to the output directory.
    """
    # Initialize config reader
    print("****")
    print("Initializing config reader...")
    configuration_reader = ConfigurationReader()
    # while running this it should call the create_configuration_file if there is no config.ini
    if not os.path.exists("config.ini"):
        print("config.ini not found. Creating a new one...")
        os.system("python create_configuration_file.py")
    elif input("would you to make a new .ini file? (y/n)") == "y":
        os.system("python create_configuration_file.py")

    config_to_use = input("please enter the exact name of your .ini file: ")

    # Load config file
    if configuration_reader.load_config_file(config_to_use):
        print("****")
        print("Reading calculation and molecular parameters...")

        # Load molecular configurations and calculation parameters
        molecular_configs = configuration_reader.get_molecular_configurations()
        calculation_params = configuration_reader.get_calculation_parameters()

        print("Calculation and molecular parameters read.")
        print("****")
        print("Initializing input generator...")
        template_path = os.path.join(os.getcwd(), 'template.orca')
        input_generator = InputGenerator()

        # Load template file
        if input_generator.load_template_file(template_path):
            # generate input file
            input_generator.generate_input_file(molecular_configs, calculation_params)
        else:
            print("Failed to load the template file. Check the path and file permissions.")

        print("Iterating over molecular configurations...\n")
        # Iterate over molecular configurations
        for config_name, molecular_config in molecular_configs.items():
            print("Generating input for " + str(config_name), "...\n")
            input_content = input_generator.generate_input_file(molecular_config, calculation_params)
            if input_content:
                print("Input content exists! Saving!!")
                output_filename = f'{config_name}.inp'
                input_generator.save_input_file(output_filename, input_content)
                try:
                    os.rename(output_filename, f"output\\{output_filename}")
                except Exception as e:
                    print(f"Error, could not move output file:{e}")
            else:
                print("No input content to add! Woe is you.\n")


if __name__ == "__main__":
    main()
