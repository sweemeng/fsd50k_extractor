# FSD50K navigator

This is a script I use to navigate the sound dataset from FSK50K. https://zenodo.org/record/4060432#.YYYJ9HtBxH4

To use this download the files from datasets. The categories is in the Ground truth file to be downloaded in the links above.

These have several script

* find_audio.py - This is the script you want
* convert.py - this only exist so that I can convert data for a Wio Terminal project. https://wiki.seeedstudio.com/Wio-Terminal-TinyML-EI-3/
* sound_category.py - this is to show the category of a file

# Usage
## Environmental variable
* set the path to the ground truth csv path
* export `export DCASE_PATH="/somepath/somewhere/FSD50K.ground_truth/dev.csv"`

## installation
* `pipenv install`
* Start the shell with `pipenv shell` then use the script as described below. 

## find_audio.py

Usage
- Basic use - `python find_audio.py categories`
- Show all label of a file - `python find_audio.py categories -s`
- Exclude file with certain categories - `python find_audio.py categories -x xcategories`
- Search Multiple file - `python find_audio.py cat1,cat2,etc`
- Search Exclude Multiple file - `python find_audio.py cat1,cat2,etc -x xcat1,xcat2`
- Help - `python find_audio.py -h`

## convert.py
Usage is similar for `find_audio.py` except for  `-p`, `-i` and `-o`
- Basic use - `python convert.py categories -p new_category_name -i source_audio_directory -o output_directory`

## sound_category.py

- Basic use - `python sound_category.py audio_name`