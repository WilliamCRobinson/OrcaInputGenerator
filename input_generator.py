"""
This module is responsible for the generation of orca inputs based on what the configuration reader reads.

Class variables

    template_file: The path or content of a template Orca input file to be used as a basis for generating new files.

    output_directory: The directory where generated Orca input files will be saved.

Class methods

    load_template_file(template_path): Loads the template Orca input file.

    generate_input_file(molecular_config, calculation_params): Generates an Orca input file based on the
                                                               given molecular configuration and calculation parameters

    save_input_file(output_path, input_content): Saves the generated input file to the specified output directory.

    set_spin_multiplicity(): this function sets the spin multiplicity according to the config files specs.

    generate_input_file(self, molecular_config, calculation_params): generates an input file based on all other specs.

"""

class InputGenerator:
    def __init__(self):
        self.template_file = None
        self.output_directory = None
        print("input generator initialized!")

    def load_template_file(self, template_path):
        print("loading template file...")
        try:
            with open(template_path, 'r') as template_file:
                self.template_file = template_file.read()
                print("Template file loaded!")
            return True
        except Exception as e:
            print(f"Error loading template file: {e}")
            return False

    def set_molecular_charge(self, charge):
        print("setting molecular charge...")
        try:
            print("molecular charge set!")
            return int(charge)

        except ValueError as e:
            print(f"Error setting molecular charge: {e}")
            return 0

    def set_spin_multiplicity(self, multiplicity):
        print("setting spin multiplicity...")
        try:
            print("spin multiplicity set!")
            return int(multiplicity)
        except ValueError as e:
            print(f"Error setting spin multiplicity: {e}")
            return 1

    # This method is really the workhorse here. # at the moment this just dumps everything
    # into what is essentially a config file

    def generate_input_file(self, molecular_config, calculation_params):
        try:
            print("writing parameters to input...")
            structure_file_path = molecular_config.get('structure_file')
            molecular_charge = self.set_molecular_charge(molecular_config.get('charge'))
            spin_multiplicity = self.set_spin_multiplicity(molecular_config.get('spin_multiplicity'))

            if not structure_file_path:
                print("Error: Structure file path not provided.")
                return None

            # Load template
            if not self.template_file:
                print("Error: Template file not loaded.")
                return None

            # Load molecular structure
            #molecular_structure = self.load_structure_from_file(structure_file_path)
            #if molecular_structure is None:
            #    print("Error: Failed to load molecular structure.")
            #    return None

            # Replace placeholders in the template with actual values
            input_content = self.template_file.format(
                basis_set=calculation_params.get('basis_set'),
                method=calculation_params.get('method'),
                convergence=calculation_params.get('convergence'),
                special_params=calculation_params.get('special'),
                structure=structure_file_path,
                charge=molecular_charge,
                multiplicity=spin_multiplicity
            )
            print("input file loaded up and ready to go!")
            return input_content
        except Exception as e:
            print(f"Error generating input file: {e}")
            return None

    def save_input_file(self, output_path, input_content):
        # Implementation to save generated input file
        print("saving input file...")
        try:
            with open(output_path, 'w') as output_file:
                output_file.write(input_content)
            print(f"***\nInput file saved to {output_path}!\n***\n")
        except Exception as e:
            print(f"Error saving input file: {e}")


# Example usage:
# input_generator = InputGenerator()
# if input_generator.load_template_file('template.orca'):
#     molecular_config = {'structure_file': 'data/molecule1.xyz', 'charge': '0', 'spin_multiplicity': '1'}
#     calculation_params = {'basis_set': '6-31G', 'method': 'B3LYP', 'convergence': '1.0e-6'}
#     input_content = input_generator.generate_input_file(molecular_config, calculation_params)
#     if input_content:
#         input_generator.save_input_file('output.orca', input_content)
