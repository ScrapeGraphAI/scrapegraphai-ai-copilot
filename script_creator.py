import os
import json

# Path to the directory containing configuration files
config_dir = "/Users/marcovinciguerra/github/scrapegraphai-ai-copilot/Configurations"

# Base directory for script files
script_base_dir = "/Users/marcovinciguerra/github/Scrapegraph-ai/examples"

# Directory for Ollama scripts
ollama_script_dir = "/Users/marcovinciguerra/github/Scrapegraph-ai/examples/local_models"

# New directory to save the updated configuration files
new_config_dir = "/Users/marcovinciguerra/github/scrapegraphai-ai-copilot/Examples"

# Loop through all files in the configuration directory
for filename in os.listdir(config_dir):
    if not filename.endswith(".json"):
        continue

    # Full path to the configuration file
    config_file_path = os.path.join(config_dir, filename)
    print(filename)

    # Load the JSON file
    with open(config_file_path, 'r') as f:
        data_list = json.load(f)

    # Iterate over each dictionary in the list
    for data in data_list:
        # Extract the script name (assuming it's in the "filename" key)
        script_name = data.get('filename')

        # Skip if there's no script name in the JSON
        if not script_name:
            continue
        if filename == "local_models_config.json":
            script_folder = ollama_script_dir
        else:
            script_folder = os.path.join(script_base_dir, os.path.splitext(filename)[0].split('_')[0])

        # Construct the script file path based on the determined script folder
        script_file_path = os.path.join(script_folder, script_name)

        try:
            # Open the corresponding script file
            with open(script_file_path, 'r') as f:
                script_content = f.read()
        except FileNotFoundError:
            print(f"File not found: {script_file_path}. Skipping.")
            continue

        # Add the script content as the "answer" property (or adjust based on your needs)
        data['answer'] = script_content

    # Save the updated JSON file to the new directory with a generic filename
    new_config_file_path = os.path.join(new_config_dir, os.path.splitext(filename)[0] + ".json")
    with open(new_config_file_path, 'w') as f:
        json.dump(data_list, f, indent=4)  # indent for better readability

    print(f"Updated configuration file saved to: {new_config_file_path}")

print("Finished processing and saving configuration files to the new directory.")

# Adding the code to remove the "filename" key from JSON files in the "Examples" folder

# Directory containing the JSON files
examples_dir = '/Users/marcovinciguerra/github/scrapegraphai-ai-copilot/Examples'

# Function to remove the "filename" key from a dictionary
def remove_filename_key(data):
    for item in data:
        if 'filename' in item:
            del item['filename']
    return data

# Iterate over all files in the directory
for filename in os.listdir(examples_dir):
    if filename.endswith('.json'):
        file_path = os.path.join(examples_dir, filename)
        
        # Open the file and load the JSON content
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Remove the "filename" key from each object in the array
        data = remove_filename_key(data)
        
        # Save the modified file
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

print("Process of removing 'filename' keys completed.")
