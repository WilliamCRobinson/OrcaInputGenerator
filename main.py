"""
Main script that will orchestrate the workflow. This script will orchestrate the generation of input files. The intent
is that this script can be easily expanded to run calculations in new workflows. Keeping it basis, you can always copy
and paste extra bits in, the main point of this is to generate large amounts of slightly varied input files.

Documentation and planning of tech specs assisted by ChatGPT 3.5. <--- very helpful but won't be taking our jobs soon

static method: set_output_directory_permissions

-William Robinson Jan 2024. Montana State University.
"""

from input_generator import InputGenerator
from configuration_reader import ConfigurationReader
import os


def set_output_directory_permissions(directory_path):
    try:
        # Check if the directory exists
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)  # Create the directory if it doesn't exist

        # Set read and write permissions (full access) for the owner
        os.chmod(directory_path, 0o700)

        print(f"Permissions for {directory_path} set successfully.")
    except Exception as e:
        print(f"Error setting permissions: {e}")


def main():
    # initialize config reader
    print("****")
    print("initializing config reader...")
    configuration_reader = ConfigurationReader()
    # load config file
    if configuration_reader.load_config_file("config.ini"):
        print("****")
        print("reading calculation and molecular parameters...")

        molecular_configs = configuration_reader.get_molecular_configurations()
        calculation_params = configuration_reader.get_calculation_parameters()

        print("calculation and molecular parameters read.")
        print("****")
        print("initializing input generator...")
        template_path = os.path.join(os.getcwd(), 'template.orca')
        input_generator = InputGenerator()
        if input_generator.load_template_file(template_path):
            # Now you can proceed with other operations, such as generating input files
            input_generator.generate_input_file(molecular_configs, calculation_params)
        else:
            print("Failed to load the template file. Check the path and file permissions.")

        print("iterating over molecular configurations...")
        # iterate over molecular configurations
        for config_name, molecular_config in molecular_configs.items():
            print("generating input for " + str(config_name), "...\n")
            input_content = input_generator.generate_input_file(molecular_config, calculation_params)
            if input_content:
                print("input content exists! saving!!")
                output_filename = f'output_{config_name}.inp'
                input_generator.save_input_file(output_filename, input_content)
                print(f"input file saved to {output_filename}")
            else:
                print("no input content to add! Woe is you.")


if __name__ == "__main__":
    output_directory_path = 'output'
    abs_output_directory_path = os.path.join(os.getcwd(), output_directory_path)
    set_output_directory_permissions(abs_output_directory_path)
    main()
