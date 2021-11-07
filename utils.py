from fsd import FSData


def fetch_files(args):
    data = FSData()
    labels = set(args.label.split(","))
    excludes = None
    if args.exclude:
        excludes = set(args.exclude.split(","))
    results = data.get_by_multiple_labels(labels, exclude=excludes)
    return results
