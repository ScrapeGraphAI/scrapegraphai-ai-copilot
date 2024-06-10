import os
import json

def extract_code(file_path):
    with open(file_path, "r") as f:
        code = f.read()

    # Extract the file name without the .py extension
    file_name = os.path.basename(file_path)[:-3]

    # Create a dictionary for the code snippet
    code_snippet = {
        "prompt": f"how is implemented {file_name}",
        "answer": code
    }

    return [code_snippet]

def main():
    # Base directory of Scrapegraph-AI (replace with your actual path)
    base_dir = "/Users/marcovinciguerra/github/Scrapegraph-ai/scrapegraphai"  # Adjust as needed

    # Output directory for JSON files
    output_dir = "/Users/marcovinciguerra/github/scrapegraphai-ai-copilot/implementation"
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

if __name__ == "__main__":
    main()
