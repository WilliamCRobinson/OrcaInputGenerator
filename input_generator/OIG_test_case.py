from input_generator import InputGenerator
from configuration_reader import ConfigurationReader

import os

# Initialize config reader
print("****")
print("Initializing config reader...")
configuration_reader = ConfigurationReader()

# Load and test with test_case_config.ini
# using geometries from
if configuration_reader.load_config_file("test_case_config.ini"):
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
