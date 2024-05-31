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
                copy_files(root / item, target)
            else:
                exception = item.suffix[1:]
                if exception:
                    exception_dir = target / exception
                    exception_dir.mkdir(parents=True, exit_ok=True)
                    shutil.copy(item, exception_dir)
    except Exception as e:
        print("Error copying")

def main():
    args = parse_args()
    args.target.mkdir(parents=True, exist_ok=True)
    copy_files(args.root, args.target)

main()