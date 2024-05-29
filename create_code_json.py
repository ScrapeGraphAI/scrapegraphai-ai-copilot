import os
import json
import re
import argparse

def get_classes_and_code(file_path):
    class_dict = {}
    with open(file_path, 'r') as file:
        code = file.read()
        class_defs = re.search(r'class\s+(\w+)\s*:', code)
        for class_name in class_defs:
            class_dict[class_name] = {
                "prompt": f"Show me the implementation of the {class_name} class in ScrapeGraphAI",
                "answer": code
            }
    return class_dict

def main(directory_path):
    json_output = {}
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                class_dict = get_classes_and_code(file_path)
                json_output.update(class_dict)
    with open('output.json', 'w') as outfile:
        json.dump(json_output, outfile, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process Python files and output a JSON with class details.')
    parser.add_argument('directory', type=str, help='The directory to process Python files in.')
    args = parser.parse_args()
    main(args.directory)
