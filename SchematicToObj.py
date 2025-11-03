import argparse
from minecraftschematics import Schematic


def main():
    parser = argparse.ArgumentParser(description='Process Minecraft schematic file.')
    parser.add_argument('file_path', help='Path to the schematic file')
    parser.add_argument('output_path', help='Run in headless mode')
    
    args = parser.parse_args()
    
    file_path = args.file_path
    headless = args.headless
    
    print(f"File path: {file_path}")
    print(f"Headless mode: {headless}")

    schematic = Schematic.load(file_path, force=True)


if __name__ == "__main__":
    main()