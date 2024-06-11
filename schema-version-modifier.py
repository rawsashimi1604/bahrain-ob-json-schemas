import os 
import json

def update_schema_version(directory, new_version):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    try:
                        data = json.load(f)
                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON from {file_path}: {e}")
                        continue

                # Update the $schema version
                if isinstance(data, dict) and "$schema" in data:
                    data["$schema"] = new_version
                    with open(file_path, 'w', encoding='utf-8') as f:
                        json.dump(data, f, indent=2)
                        print(f"Updated $schema version in {file_path}")

if __name__ == "__main__":
    update_schema_version("pisp", "https://json-schema.org/draft-07/schema")