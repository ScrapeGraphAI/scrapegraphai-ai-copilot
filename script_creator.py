import os
import json

def extract_code(file_path):
    with open(file_path, "r") as f:
        code = f.read()

    # Extract the file name without the .py extension
    file_name = os.path.basename(file_path)[:-3]

    # Create a dictionary for the code snippet
    code_snippet = {
        "prompt": f"how is {file_name} implemented in Scrapegraphai?",
        "answer": code
    }

    return [code_snippet]

def process_base_directory(base_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Debugging: Print folder names before processing
    print("Processing folders:")

    # Loop through each item in the base directory, ignoring hidden files
    for item in os.listdir(base_dir):
        if item in [".git", ".idea", "__pycache__"] or item.startswith("."):
            continue

        item_path = os.path.join(base_dir, item)

        # Check if the item is a directory
        if os.path.isdir(item_path):
            # Print the folder name being processed
            print(f"  - {item}")

            # Loop through each Python file in the directory, excluding __init__.py
            for file in os.listdir(item_path):
                if file.endswith(".py") and not file.startswith("__init__"):
                    file_path = os.path.join(item_path, file)

                    try:
                        # Extract the entire code and create a list with one dictionary
                        code_snippets = extract_code(file_path)

                        # Create a filename for the JSON file (use folder and script name)
                        output_file = os.path.join(output_dir, f"{item}_{os.path.splitext(file)[0]}.json")

                        # Save the list of dictionaries as a JSON file with indentation
                        with open(output_file, "w") as f:
                            json.dump(code_snippets, f, indent=4)
                    except FileNotFoundError:
                        print(f"File not found: {file_path}. Skipping.")
        else:
            print(f"Skipping non-directory item: {item}")

def process_configuration_files(config_dir, script_base_dir, ollama_script_dir, new_config_dir):
    if not os.path.exists(new_config_dir):
        os.makedirs(new_config_dir)

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

def remove_filename_key_from_examples(examples_dir):
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

def main():
    # Define paths
    base_dir = "/home/vedo/Documents/GitHub/Scrapegraph-ai/scrapegraphai"
    output_dir = "/home/vedo/Documents/GitHub/scrapegraphai-ai-copilot/implementation"
    config_dir = "/home/vedo/Documents/GitHub/scrapegraphai-ai-copilot/Configurations"
    script_base_dir = "/home/vedo/Documents/GitHub/Scrapegraph-ai/examples"
    ollama_script_dir = "/home/vedo/Documents/GitHub/Scrapegraph-ai/examples/local_models"
    new_config_dir = "/home/vedo/Documents/GitHub/scrapegraphai-ai-copilot/Examples"
    examples_dir = new_config_dir

    # Process base directory
    process_base_directory(base_dir, output_dir)
    
    # Process configuration files
    process_configuration_files(config_dir, script_base_dir, ollama_script_dir, new_config_dir)
    
    # Remove filename key from examples
    remove_filename_key_from_examples(examples_dir)

if __name__ == "__main__":
    main()
