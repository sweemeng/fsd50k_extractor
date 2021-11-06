from dcase import DCaseData


def fetch_files(args):
    data = DCaseData()
    labels = set(args.label.split(","))
    excludes = None
    if args.exclude:
        excludes = set(args.exclude.split(","))
    results = data.get_by_multiple_labels(labels, exclude=excludes)
    return results
