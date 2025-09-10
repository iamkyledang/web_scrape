import os
import shutil
import subprocess
import time
import random
from concurrent.futures import ThreadPoolExecutor

def delete_playwright_temp_folders():
    temp_dir = os.path.join(os.getenv('TEMP'))
    for folder_name in os.listdir(temp_dir):
        if folder_name.startswith('playwright_firefoxdev_profile'):
            folder_path = os.path.join(temp_dir, folder_name)
            if os.path.isdir(folder_path):
                shutil.rmtree(folder_path)
                print(f"Deleted temporary folder: {folder_path}")

def run_script():
    while True:
        try:
            # Run the main.py script
            result = subprocess.run(['python', 'main.py'], check=True)
            print("main.py ran successfully.")
            break  # Exit the loop if the script runs successfully
        except subprocess.CalledProcessError:
            print("main.py encountered an error. Retrying in 5 to 10 seconds...")
            time.sleep(random.uniform(5, 10))
    print("Completed!")

# Delete Playwright temporary folders before running the scripts
delete_playwright_temp_folders()

# Create a ThreadPoolExecutor to run 3 instances concurrently
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(run_script) for _ in range(10)]

# Wait for all futures to complete
for future in futures:
    future.result()