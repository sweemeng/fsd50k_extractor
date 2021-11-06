import argparse

import audio
from utils import fetch_files


def main():
    parser = argparse.ArgumentParser(description="get file by labels")
    parser.add_argument("label", metavar="label", type=str, help="label used by dataset")
    parser.add_argument("-p", "--primary-labels", action="store", type=str, help="set primary category")
    parser.add_argument("-i", "--input-dir", action="store", type=str, help="set input path")
    parser.add_argument("-o", "--output-dir", action="store", type=str, help="set output path")
    parser.add_argument("-x", "--exclude", action="store", type=str, help="exclude options")
    args = parser.parse_args()
    results = fetch_files(args)

    for item in results:
        
        audio.convert_file(item, args.primary_labels, args.input_dir, args.output_dir)


if __name__ == "__main__":
    main()
