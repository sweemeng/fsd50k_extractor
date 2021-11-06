import os.path

import librosa
import soundfile as sf

INPUT_DIR = "/media/sweemeng/New Volume/fsk50k/fsd50k/FSD50K.dev_audio/"
OUTPUT_DIR = "/media/sweemeng/New Volume/wiosound_data"


def resample(input_file, output_file):
    data, sample_rate = librosa.load(input_file, sr=16000)
    sf.write(output_file, data, sample_rate)


def convert_file(audio_file, category=None, input_dir=INPUT_DIR, output_dir=OUTPUT_DIR):
    if category:
        filename = f"{category}.{audio_file}"
    else:
        filename = audio_file
    output_path = os.path.join(output_dir, filename)
    input_path = os.path.join(input_dir, audio_file)
    resample(input_path, output_path)
