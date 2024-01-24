import json
import subprocess
from concurrent.futures import ThreadPoolExecutor

def run_command(icon_path, folder_path):
    command = f"python ./app_icon_genrator.py {icon_path} {folder_path}"
    subprocess.run(command, shell=True)

def process_json(json_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    # Using ThreadPoolExecutor to run commands in parallel
    with ThreadPoolExecutor() as executor:
        # Submit each command for parallel execution
        futures = [executor.submit(run_command, entry['icon_path'], entry['folder_path']) for entry in data]

        # Wait for all commands to complete
        for future in futures:
            future.result()

if __name__ == "__main__":
    import sys

    # Check if the correct number of command-line arguments is provided
    json_file_path = 'data.json'
    
    if len(sys.argv) == 2:
        json_file_path = sys.argv[1]
    process_json(json_file_path)
