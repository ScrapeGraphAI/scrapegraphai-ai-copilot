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

        # Determine the script folder based on the filename
        if script_name.lower() == "ollama":
            script_folder = ollama_script_dir  # Use the Ollama script directory
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