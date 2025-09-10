# Web Scrape Project

This project is designed to automate the extraction of students' information by their IDs from the Van Lang University website, with robust error handling and support for concurrent execution. It is intended for use in environments where large numbers of student IDs need to be checked, processed, or validated, such as academic or institutional data collection.

## Main Purpose
The tool scrapes and saves students' information from the Van Lang University admissions website by iterating through a list of student IDs. It is robust to errors and can run multiple concurrent scraping sessions for efficiency.


## Project Structure and Main Files

- **main.py**
  - The primary script for running the scraping logic. It reads student IDs from `numbers.txt` (or `social_shuffled.txt` as configured in the script), queries the Van Lang University website for each ID, and saves the resulting HTML for each student found. IDs not found or with errors are logged in `missing.txt`, and successfully checked IDs are logged in `checked.txt`.

- **multiple.py**
  - A utility script that manages the concurrent execution of `main.py` using a thread pool. It also handles the cleanup of temporary Playwright browser profiles before execution. This script is useful for running multiple instances of the main process in parallel, increasing throughput and reliability.

- **numbers.txt**
  - A text file containing a list of student IDs to be processed. Each line represents a single student ID. (Note: The script may also use `social_shuffled.txt` as the input file, so ensure the correct file is referenced in `main.py`.)

- **missing.txt**
  - A text file containing a list of IDs that were not found or encountered errors during scraping. Each line represents a single ID. This file is updated automatically by the script.

- **checked.txt**
  - A text file containing a list of IDs that have already been checked or processed. This helps prevent duplicate work and allows the process to resume efficiently if interrupted.


## How It Works

1. **Preparation**: Place the list of student IDs to be checked in `numbers.txt` (or the file referenced in `main.py`, e.g., `social_shuffled.txt`).
2. **Execution**: Run `multiple.py` to start multiple concurrent instances of `main.py`. The script will automatically clean up Playwright temporary folders before starting.
3. **Scraping**: Each instance of `main.py` will read IDs from the input file, check if they have already been processed (using `checked.txt`), and then attempt to scrape the student's information from the Van Lang University website.
4. **Logging**: Successfully processed IDs are appended to `checked.txt`. IDs not found or with errors are appended to `missing.txt`.
5. **Completion**: Once all IDs are processed, the results will be reflected in `checked.txt` and `missing.txt`.

## Notes
- The project uses Playwright (as inferred from the temp folder cleanup), so ensure all dependencies are installed.
- Adjust the number of concurrent workers in `multiple.py` as needed for your system's capabilities.
- The scripts are designed for Windows environments (uses `%TEMP%` and PowerShell conventions).


## Relevant Files Summary
- `main.py` — Main scraping/processing logic
- `multiple.py` — Concurrent execution and error handling
- `numbers.txt` — List of student IDs to process (or `social_shuffled.txt` as referenced in the script)
- `missing.txt` — List of IDs not found or with errors
- `checked.txt` — List of processed IDs

---

For any questions or issues, please refer to the code comments or contact the project maintainer.
