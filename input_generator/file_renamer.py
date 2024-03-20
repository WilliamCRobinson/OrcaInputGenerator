import os

def rename_files(directory, old_part, new_part):
    for filename in os.listdir(directory):
        if old_part in filename:
            new_filename = filename.replace(old_part, new_part)
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            os.rename(old_path, new_path)
            print(f"Renamed '{filename}' to '{new_filename}'")

# Replace 'old_part' with the part you want to replace
old_part = input("what is the old phrase you want replaced in file name:")
# Replace 'new_part' with the part you want to replace 'old_part' with
new_part = input("what is the new phrase you want replaced in file name:")
# Replace 'directory_path' with the path of the directory containing the files
directory_path = input("Specify directory to do changes to:")

rename_files(directory_path, old_part, new_part)
