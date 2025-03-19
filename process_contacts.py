import pandas as pd

def process_contacts(file_path):
    try:
        print(f"Attempting to read: {file_path}")
        data = pd.read_csv(file_path,  encoding='latin1')
        print(f"Found {len(data)} contacts.")
        for name in data['name']:
            print(f"Would send LinkedIn connection request to: {name}")
        print("Process complete.")
    except FileNotFoundError:
        print(f"File {file_path} not found. Make sure the file is in the repository root.")
    except Exception as e:
        print(f"Error processing contacts: {e}")

if __name__ == "__main__":
    process_contacts("linkedin.csv")
