import os
import zipfile

import pandas as pd

df = pd.read_excel('./x.xlsx', engine='openpyxl')
second_column = df.iloc[:, 1]
titles = second_column.tolist()


def create_folders_with_index(titles):
    for index, title in enumerate(titles, start=1):
        folder_name = f"{index:02d}_{title.replace(' ', '_').replace(':', '').replace('&', 'and').replace('!', '')}"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Folder '{folder_name}' created.")
        else:
            print(f"Folder '{folder_name}' already exists.")


def zip_folders(titles):
    for index, title in enumerate(titles, start=1):
        folder_name = f"{index:02d}_{title.replace(' ', '_').replace(':', '').replace('&', 'and').replace('!', '')}"
        zip_filename = os.path.join(folder_name, f"{folder_name}.zip")
        
        # Remove the existing zip file if it exists
        if os.path.exists(zip_filename):
            os.remove(zip_filename)
            print(f"Existing zip file '{zip_filename}' removed.\n")
        
        # Create a new zip file inside the folder
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(folder_name):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, folder_name))
        print(f"Folder '{folder_name}' has been zipped into '{zip_filename}'.\n")

import subprocess

def run_git_commands():
    try:
        # Navigate to your repository (if needed)
        # subprocess.run(["cd", "/path/to/your/repo"], check=True)

        # Add all files
        subprocess.run(["git", "add", "."], check=True)

        # Commit with a message
        subprocess.run(["git", "commit", "-m", "update_files"], check=True)

        # Push to the remote repository
        subprocess.run(["git", "push"], check=True)

        print("Git commands executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# create_folders_with_index(titles)
zip_folders(titles)
run_git_commands()