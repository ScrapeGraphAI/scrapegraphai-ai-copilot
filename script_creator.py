import os
import json

# Load the JSON file
with open('/Users/marcovinciguerra/github/scrapegraphai-ai-copilot/Examples/anthropic_config.json', 'r') as f:
    data = json.load(f)

# Loop through each object in the list
for obj in data:
    # Check if the filename is empty (i.e., no script to copy)
    if not obj['filename']:
        continue

    # Open the corresponding script file
    script_file_path = '/Users/marcovinciguerra/github/Scrapegraph-ai/examples/anthropic/' + obj['filename']
    with open(script_file_path, 'r') as f:
        script_content = f.read()

    # Add the script content as the "answer" property in the JSON object
    obj['answer'] = script_content

    # Remove the "filename" key from the JSON object
    del obj['filename']

# Create a new JSON file named anthropic.json
with open('/Users/marcovinciguerra/github/scrapegraphai-ai-copilot/Examples/anthropic.json', 'w') as f:
    json.dump(data, f, indent=4)
