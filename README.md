# Sortify 📁

**Sortify** is a lightweight Python command-line tool that automatically organizes files into categorized directories based on their file extensions.

Instead of manually sorting files, Sortify scans a directory and moves supported files into folders such as `images`, `sheets`, `word`, `bash`, and `files`.

## ✨ Features

- Automatically organizes files by extension.
- Creates destination directories when they don't exist.
- Supports multiple file types.
- Skips unsupported file extensions.
- Prevents overwriting files when a destination filename already exists.
- Handles common filesystem errors.
- Simple command-line interface.

## 📂 Supported File Types

| Category | Extensions |
|---|---|
| Images | `.jpg`, `.jpeg`, `.png` |
| Spreadsheets | `.xls`, `.xlsx` |
| Text files | `.txt` |
| Word documents | `.docx` |
| Shell scripts | `.sh` |

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or later
- Git

### Installation

Clone the repository:

```bash
git clone https://github.com/itachi0xx/Sortify.git
```

Navigate to the project directory:

```bash
cd Sortify
```

### Usage

Run the program:

```bash
python main.py
```

Replace `main.py` with your actual Python filename if it is different.

When prompted, enter the path of the directory you want to organize:

```text
Enter directory path: /path/to/your/folder
```

Sortify will scan the directory, create the required folders, and move supported files into their corresponding categories.

## 📁 Example

**Before:**

```text
Downloads/
├── photo.jpg
├── report.docx
├── data.xlsx
├── notes.txt
└── script.sh
```

**After:**

```text
Downloads/
├── images/
│   └── photo.jpg
├── word/
│   └── report.docx
├── sheets/
│   └── data.xlsx
├── files/
│   └── notes.txt
└── bash/
    └── script.sh
```

## 🛠️ Built With

- **Python** — Main programming language.
- **pathlib** — Filesystem path handling.
- **shutil** — Moving files between directories.

## ⚠️ Notes

- Sortify currently organizes files in the specified directory, not recursively through its subdirectories.
- Unsupported file types are skipped.
- If a file with the same name already exists in the destination folder, the new file is skipped.
- Consider backing up important files before running any file-organizing tool.

## 🗺️ Future Improvements

- [ ] Add support for more file extensions.
- [ ] Add recursive directory scanning.
- [ ] Add command-line arguments.
- [ ] Add a dry-run mode to preview changes.
- [ ] Add logging and a summary report.
- [ ] Add automated tests.

## 👨‍💻 Author

**itachi0xx**

GitHub: [@itachi0xx](https://github.com/itachi0xx)

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
