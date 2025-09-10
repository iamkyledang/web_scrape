# Web Scrape Project

This project is designed to automate the extraction of students' information by their IDs, with robust error handling and support for concurrent execution. It is intended for use in environments where large numbers of student IDs need to be checked, processed, or validated, such as academic or institutional data collection.

## Project Structure and Main Files

- **main.py**
  - The primary script for running the scraping or processing logic. This script is executed by the automation and concurrency tools in the project.

- **multiple.py**
  - A utility script that manages the concurrent execution of `main.py` using a thread pool. It also handles the cleanup of temporary Playwright browser profiles before execution. This script is useful for running multiple instances of the main process in parallel, increasing throughput and reliability.

- **missing.txt**
  - A text file containing a list of IDs that are missing or need to be processed. Each line represents a single ID. This file is used as an input source for the scraping or checking logic.

- **checked.txt**
  - A text file containing a list of IDs that have already been checked or processed. This helps prevent duplicate work and allows the process to resume efficiently if interrupted.

## How It Works

1. **Preparation**: Ensure that `missing.txt` contains the IDs you want to process. IDs already processed should be in `checked.txt`.
2. **Execution**: Run `multiple.py` to start multiple concurrent instances of `main.py`. The script will automatically clean up Playwright temporary folders before starting.
3. **Error Handling**: If `main.py` encounters an error, `multiple.py` will retry the process after a short random delay, ensuring robustness.
4. **Completion**: Once all IDs are processed, the results will be reflected in `checked.txt`.

## Notes
- The project uses Playwright (as inferred from the temp folder cleanup), so ensure all dependencies are installed.
- Adjust the number of concurrent workers in `multiple.py` as needed for your system's capabilities.
- The scripts are designed for Windows environments (uses `%TEMP%` and PowerShell conventions).

## Relevant Files Summary
- `main.py` — Main scraping/processing logic
- `multiple.py` — Concurrent execution and error handling
- `missing.txt` — List of IDs to process
- `checked.txt` — List of processed IDs

---

For any questions or issues, please refer to the code comments or contact the project maintainer.
