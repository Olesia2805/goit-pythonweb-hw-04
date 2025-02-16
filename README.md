# Async File Copier

## Description
This script recursively scans a source folder, reads all files within it (including subdirectories), and copies them into a target folder. Each file is placed in a subdirectory within the target folder based on its file extension. The script runs asynchronously for efficiency and logs the file operations.

## Usage
Run the script with the following command:
```sh
python main.py --source <source_folder> --output <output_folder>
```
```sh
main.py -s -o
```
Where:
- `--source <source_folder>` specifies the path to the folder containing files to be copied. If not provided, **it defaults to "source"**.
- `--output <output_folder>` specifies the path to the folder where files will be copied, organized by extension. If not provided, **it defaults to "output"**.

## Functionality Breakdown
1. Created an ArgumentParser object to process command line arguments.
2. Added the necessary arguments to specify the source and destination folders.
3. Initialized asynchronous paths for the source and destination folders.
4. Wrote an asynchronous function `read_folder` that recursively reads all files in the source folder and its subfolders.
5. Wrote an asynchronous function `copy_file` that copies each file to the corresponding subfolder in the destination folder based on its extension.
6. Configured error logging.

## Example Output
Upon running the script, you will see logs like:
```
%(asctime)s - %(levelname)s - %(message)s
YYYY-MM-DD HH:MM:SS,343 - INFO - Copied: file.txt -> output/txt/file.txt
YYYY-MM-DD HH:MM:SS,343 - INFO - Processed NUMBERS files.
```

## Notes
- If a file has no extension, it will be placed in an `unknown` directory.
- Existing files in the target folder are **not overwritten**.
