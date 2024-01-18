Documentation for Orca Input Generator

William Robinson 2024

Project Overview:

The project involves creating a Python program that generates input files for the quantum chemistry software Orca. The
program is designed to handle multiple input configurations at once, each with different molecular geometries, charges,
and spin multiplicities. The program can do one calculation type and many geometries. Its not too inconvenient to set up
multiple config files for each of your calc types.

Project Structure:

1.	Input Generator Module (input_generator.py):
    o	Responsibility: Generates Orca input files based on provided molecular configurations and calculation
                        parameters.
        o	Methods:
            	load_template_file(template_path): Loads the template Orca input file.
            	load_structure_from_file(file_path): Loads the molecular structure from an XYZ file.
            	set_molecular_charge(charge): Sets the molecular charge for the structure.
            	set_spin_multiplicity(multiplicity): Sets the spin multiplicity for the structure.
            	generate_input_file(molecular_config, calculation_params): Generates an Orca input file based on the
                                                                           given molecular configuration and calculation
                                                                           parameters.
            	save_input_file(output_path, input_content): Saves the generated input file to the specified output
                directory.


2.	Configuration Reader Module (config_reader.py):
    o	Responsibility: Reads the configuration file containing molecular configurations and calculation parameters.
        o	Methods:
            	load_config_file(file_path): Reads and parses the configuration file.
            	get_molecular_configurations(): Retrieves a dictionary of molecular configurations.
            	get_calculation_parameters(): Retrieves a dictionary of calculation parameters.

Dependencies:

    ASE (Atomic Simulation Environment) for XYZ file parsing (pip install ase).

Notes:

    The project assumes that XYZ files are generated from Orca and are compatible.
    Adjust the template file and placeholders based on your specific Orca input file format and requirements.
    Ensure that the required files (template, XYZ files, configuration file) are present in the specified paths

Planned Functionality:

The ability to specify SBDFT jobs and TDDFT jobs with unique flip-spins and finalMS. This will probably involve adding
some if statements to the generate_input_file would be nice if we just had to specify a path to an xyz file in the
config.ini file.

Using this python package:

Basically, dump all your geometries into the data directory, then set up a configuration file copy and paste all your
file names into there, specify the parameters and the program should write everything according to the template from
there.

1. make all your xyz files.
2. put all them in the data directory in this python package.
3. set up config.ini with what type of calculation you would like to run on these geometries.
4. run the python program.
5. Check the output directory for your new orca inputs, add in extra blocks as needed.

Project File structure

project_root/
│
├── quantum_chemistry/
│   ├── __init__.py
│   ├── input_generator.py
│   ├── config_reader.py
│   └── main.py
│
├── template.orca
├── config.ini
├── data/
│   ├── molecule1.xyz
│   └── molecule2.xyz
│
└── output/

see the default config.ini and the template.orca file (which can be adjusted)
