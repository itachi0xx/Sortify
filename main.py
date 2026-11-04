import shutil
from pathlib import Path


def path_content(path):
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Directory does not exist: {path}")

    if not path.is_dir():
        raise NotADirectoryError(f"Not a directory: {path}")

    content = []

    try:
        for c in path.iterdir():
            if c.is_file():
                content.append(c)

    except PermissionError:
        raise PermissionError(f"Cannot access directory: {path}")

    except OSError as e:
        raise OSError(f"Could not scan directory: {e}")

    return content


def files_extension(content):
    for file in content:
        yield f"{file.name} -> {file.suffix}"


def create_dirs(path):
    names = ["images", "files", "sheets", "bash", "word"]
    parent_dir = Path(path)

    for name in names:
        try:
            (parent_dir / name).mkdir(parents=True, exist_ok=True)

        except PermissionError:
            print(f"Permission denied: {parent_dir / name}")

        except OSError as e:
            print(f"Could not create directory {name}: {e}")


def organize_files(files_paths, path):
    path = Path(path)

    ext_map = {
        ".jpg": "images",
        ".jpeg": "images",
        ".png": "images",
        ".xls": "sheets",
        ".xlsx": "sheets",
        ".txt": "files",
        ".docx": "word",
        ".sh": "bash",
    }

    for file in files_paths:
        dest = ext_map.get(file.suffix.lower())

        if not dest:
            print(f"[SKIPPED] Unsupported file: {file.name}")
            continue

        destination = path / dest / file.name

        if destination.exists():
            print(f"[SKIPPED] File already exists: {file.name}")
            continue

        try:
            shutil.move(str(file), str(destination))
            print(f"[OK] {file.name} -> {dest}/")

        except PermissionError:
            print(f"[ERROR] Permission denied: {file.name}")

        except FileNotFoundError:
            print(f"[ERROR] File not found: {file.name}")

        except shutil.Error as e:
            print(f"[ERROR] Could not move {file.name}: {e}")

        except OSError as e:
            print(f"[ERROR] Filesystem error: {e}")


def main():
    try:
        path = input("Enter directory path: ").strip()

        if not path:
            raise ValueError("Directory path cannot be empty")

        content = path_content(path)

        create_dirs(path)

        organize_files(content, path)

        print("\nOrganization completed!")

    except ValueError as e:
        print(f"[INPUT ERROR] {e}")

    except (FileNotFoundError, NotADirectoryError, PermissionError) as e:
        print(f"[DIRECTORY ERROR] {e}")

    except OSError as e:
        print(f"[SYSTEM ERROR] {e}")

    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")


if __name__ == "__main__":
    main()
