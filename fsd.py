import csv
import os

# DATA_PATH = "/media/sweemeng/New Volume/fsk50k/fsd50k/FSD50K.ground_truth/dev.csv"
DATA_PATH=os.getenv("FSD_PATH")


class FSData:
    def __init__(self, path=DATA_PATH):
        self.data_map = {}
        self.path = path

    def get_by_labels(self, target):
        results = []
        with open(self.path) as csv_file:
            reader = csv.DictReader(csv_file)
            for item in reader:
                labels = item["labels"].split(",")
                if target in labels:
                    results.append(f"{item['fname']}.wav")
        return results

    def get_by_multiple_labels(self, targets, exclude=None):
        if exclude is None:
            exclude = set()
        results = []
        with open(self.path) as csv_file:
            reader = csv.DictReader(csv_file)
            for item in reader:
                labels = set(item["labels"].split(","))
                if targets.issubset(labels):
                    if exclude and (exclude & labels):
                        continue
                    results.append(f"{item['fname']}.wav")
        return results

    def get_sound_category(self, audio_id):
        results = None
        if "wav" in audio_id:
            audio_id = audio_id.split(".")[0]
        with open(self.path) as csv_file:
            reader = csv.DictReader(csv_file)
            for item in reader:
                if item['fname'] == audio_id:
                    results = item['labels']

        return results
