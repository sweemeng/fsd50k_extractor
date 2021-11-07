import argparse

import utils
from fsd import FSData


def main():
    parser = argparse.ArgumentParser(description="get file by labels")
    parser.add_argument("label", metavar="label", type=str, help="label used by dataset")
    parser.add_argument("-s", "--show-labels", action="store_true", help="show category of file")
    parser.add_argument("-x", "--exclude", action="store", type=str, help="exclude options")
    data = FSData()
    args = parser.parse_args()
    results = utils.fetch_files(args)

    for item in results:
        print(item)
        if args.show_labels:
            print(data.get_sound_category(item))


if __name__ == "__main__":
    main()
