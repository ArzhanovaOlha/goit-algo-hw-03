from pathlib import Path
import argparse
import shutil

def parse_args():
    parser = argparse.ArgumentParser(description='Copy the items')
    parser.add_argument('--root', type= Path, required=True, help='Path to source')
    parser.add_argument('--target', type= Path, default=Path('dist'), help='Path to target')
    return parser.parse_args()

def copy_files(root, target):
    try:
        for item in root.iterdir():
            if item.is_dir():
                copy_files(item, target)
            else:
                extension = item.suffix[1:]
                if extension:
                    extension_dir = target / extension
                    extension_dir.mkdir(parents=True, exist_ok=True)
                    shutil.copy(item, extension_dir)
            
    except Exception as e:
        print(f"Error copying {e}")

def main():
    args = parse_args()
    args.target.mkdir(parents=True, exist_ok=True)
    copy_files(args.root, args.target)

main()