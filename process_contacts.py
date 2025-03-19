import pandas as pd

def process_contacts(file_path):
    try:
        data = pd.read_csv(file_path)
        for name in data['name']:
            print(f"Would send LinkedIn connection request to: {name}")
        print("Process complete.")
    except Exception as e:
        print(f"Error processing contacts: {e}")

if __name__ == "__main__":
    process_contacts("contacts.csv")
