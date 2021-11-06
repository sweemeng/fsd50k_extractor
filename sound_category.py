import argparse

from dcase import DCaseData


def main():
    parser = argparse.ArgumentParser(description="get file by sound id")
    parser.add_argument("sound_id", metavar="sound_id", type=str, help="label used by dataset")
    args = parser.parse_args()
    data = DCaseData()
    results = data.get_sound_category(args.sound_id)
    print(results)


if __name__ == "__main__":
    main()
