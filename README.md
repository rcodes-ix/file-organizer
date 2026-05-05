# File Organizer (Python Script)

A Python-based automation tool that organizes files in a selected directory by sorting them into categorized folders based on file extensions. It helps keep folders clean and structured without manual sorting.

---

## Features

- Automatically organizes files by type
- Supports images, PDFs, executables, and other file types
- Creates category folders automatically if they don’t exist
- Prevents file overwriting by renaming duplicates
- Lightweight script with no external dependencies

---

## How It Works

- The user provides a folder path when running the script
- The script scans all files inside the folder
- Each file is checked based on its extension
- Files are moved into categorized folders:
  - Images → .png, .jpg, .jpeg
  - Softwares → .exe
  - PDFs → .pdf
  - Others → everything else
- If a file with the same name already exists in the destination folder, the script renames the new file by adding a number suffix

---

## Installation & Usage

Clone the repository:```git clone https://github.com/rcodes-ix/file-organizer.git```

Navigate to the folder:```cd file-organizer```

Run the script:```python organizer.py```

When prompted, enter the folder path:
Enter folder path: ```C:\Users\YourName\Downloads```

---

## Project Structure

```organizer.py```   → Main file organization logic

```README.md```     → Project documentation

---

## Example

Before running the script:
Downloads/
- image.png
- setup.exe
- document.pdf
- notes.txt

After running the script:
Downloads/
- Images/
  - image.png
- Softwares/
  - setup.exe
- PDFs/
  - document.pdf
- Others/
  - notes.txt

---

## Limitations

- No graphical interface (CLI only)
- Requires manual folder path input
- No undo feature after moving files
- Basic file type classification only

---

## Future Improvements

- Add GUI version
- Add undo/restore feature
- Add configurable file rules (JSON config)
- Improve file type detection
- Add logging system

---

## Author

Created by Rekik Samson
