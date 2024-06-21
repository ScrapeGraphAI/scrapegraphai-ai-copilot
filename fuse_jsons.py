import os
import json
import sys

def fuse_json_files(folders, output_file):
    # Initialize an empty list to store the objects from the JSON files
    objects = []

    # Iterate over the folders
    for folder in folders:

        # Iterate over the files in the folder
        for file_name in os.listdir(folder):

            # Check if the file is a JSON file
            if file_name.endswith('.json'):

                # Get the full path of the file
                file_path = os.path.join(folder, file_name)

                # Open the file and load the JSON data
                with open(file_path, 'r') as file:
                    data = json.load(file)

                # Iterate over the objects in the JSON data
                for obj in data:

                    # Check if the object has the same schema as the first object
                    if objects and set(obj.keys()) != set(objects[0].keys()):
                        raise ValueError(f'The objects in the JSON file "{file_name}" do not have the same schema.')

                    # Add the object to the list
                    objects.append(obj)

    # Open the output file and write the JSON data
    with open(output_file, 'w') as file:
        json.dump(objects, file)

def main():
    # Get the list of folders from the command line arguments
    folders = [os.path.abspath(folder) for folder in sys.argv[1:]]

    # Get the path of the output file from the user
    output_file = "dataset.json"
    output_file = os.path.abspath(output_file)

    # Fuse the JSON files
    fuse_json_files(folders, output_file)

    # Print a success message
    print(f'The JSON files have been successfully fused into {output_file}')

if __name__ == '__main__':
    main()
