class InputGenerator:
    """
    InputGenerator class is responsible for generating input files for Orca calculations based on a template file.

    Attributes:
        template_file (str): The content of the template Orca input file.
        output_directory (str): The directory where generated Orca input files will be saved.

    Methods:
        __init__(): Initializes an instance of the InputGenerator class.

        load_template_file(template_path: str) -> bool:
            Loads the template Orca input file from the specified path.

        set_molecular_charge(charge: str) -> int:
            Sets the molecular charge and returns the integer value.

        set_spin_multiplicity(multiplicity: str) -> int:
            Sets the spin multiplicity and returns the integer value.

        generate_input_file(molecular_config: dict, calculation_params: dict) -> str:
            Generates an Orca input file based on molecular configuration and calculation parameters.

        save_input_file(output_path: str, input_content: str):
            Saves the generated input file to the specified output path.
    """
    def __init__(self):
        """
        Initializes an instance of the InputGenerator class.
        """
        self.template_file = None
        self.output_directory = None
        print("Input generator initialized!")

    def load_template_file(self, template_path: str) -> bool:
        """
        Loads the template Orca input file from the specified path.

        Args:
            template_path (str): Path to the template Orca input file.

        Returns:
            bool: True if the file is successfully loaded, False otherwise.
        """
        try:
            with open(template_path, 'r') as template_file:
                self.template_file = template_file.read()
                print("Template file loaded!")
            return True
        except Exception as e:
            print(f"Error loading template file: {e}")
            return False

    def set_molecular_charge(self, charge: str) -> int:
        """
        Sets the molecular charge and returns the integer value.

        Args:
            charge (str): Molecular charge as a string.

        Returns:
            int: The integer value of the molecular charge.
        """
        print("Setting molecular charge...")
        try:
            print("Molecular charge set!")
            return int(charge)
        except ValueError as e:
            print(f"Error setting molecular charge: {e}")
            return 0

    def set_spin_multiplicity(self, multiplicity: str) -> int:
        """
        Sets the spin multiplicity and returns the integer value.

        Args:
            multiplicity (str): Spin multiplicity as a string.

        Returns:
            int: The integer value of the spin multiplicity.
        """
        print("Setting spin multiplicity...")
        try:
            print("Spin multiplicity set!")
            return int(multiplicity)
        except ValueError as e:
            print(f"Error setting spin multiplicity: {e}")
            return 1

    def generate_input_file(self, molecular_config: dict, calculation_params: dict) -> str:
        """
        Generates an Orca input file based on molecular configuration and calculation parameters.

        Args:
            molecular_config (dict): Molecular configuration.
            calculation_params (dict): Calculation parameters.

        Returns:
            str: Content of the generated Orca input file.
        """
        try:
            print("Writing parameters to input...")
            structure_file_path = molecular_config.get('structure_file')
            molecular_charge = self.set_molecular_charge(molecular_config.get('charge'))
            spin_multiplicity = self.set_spin_multiplicity(molecular_config.get('spin_multiplicity'))

            if not structure_file_path:
                print("Error: Structure file path not provided.")
                return None

            # Replace placeholders in the template with actual values
            input_content = self.template_file.format(
                basis_set=calculation_params.get('basis_set'),
                method=calculation_params.get('method'),
                convergence=calculation_params.get('convergence'),
                special_params=calculation_params.get('special'),
                DFT_functional=calculation_params.get('dftfunctional'),
                structure=structure_file_path,
                charge=molecular_charge,
                multiplicity=spin_multiplicity
            )
            print("Input file loaded up and ready to go!")
            return input_content
        except Exception as e:
            print(f"Error generating input file: {e}")
            return None

    def save_input_file(self, output_path: str, input_content: str):
        """
        Saves the generated input file to the specified output path.

        Args:
            output_path (str): Path to save the generated input file.
            input_content (str): Content of the generated input file.
        """
        print("Saving input file...")
        try:
            with open(output_path, 'w') as output_file:
                output_file.write(input_content)
            print(f"Input file saved to {output_path}!")
        except Exception as e:
            print(f"Error saving input file: {e}")


