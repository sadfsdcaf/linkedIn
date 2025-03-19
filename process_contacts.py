import pandas as pd

def process_contacts(file_path):
    try:
        print(f"Attempting to read: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        print(f"Found {len(lines)} contacts.")
        for line in lines:
            name = line.strip()
            if name:
                print(f"Would send LinkedIn connection request to: {name}")
        print("Process complete.")

    except FileNotFoundError:
        print(f"File {file_path} not found. Make sure the file is in the repository root.")
    except Exception as e:
        print(f"Error processing contacts: {e}")

if __name__ == "__main__":
    process_contacts("linkedin.txt")
