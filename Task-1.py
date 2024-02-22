from pathlib import Path 
import shutil
import argparse

def recurcive_sort(source: Path, destination: Path = Path("dist")) -> None:
    for elem in source.iterdir():
        try:
            if elem.is_file():
                subdir = destination / elem.suffix.lower()
                subdir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(elem, subdir)

            elif elem.is_dir():
                recurcive_sort(elem, destination)
        except (PermissionError, OSError, shutil.Error) as e:
            print(f"Error processing {elem}: {e}")

def main():
    parser = argparse.ArgumentParser(description='Recursive sort and copy files')
    parser.add_argument('source', type=Path, help='Path to the source directory')
    parser.add_argument('--destination', type=Path, default=Path("dist"), help='Path to destination directory')
    
    args = parser.parse_args()
    source = args.source
    destination = args.destination
    recurcive_sort(source, destination)

if __name__ == "__main__":
    main()

