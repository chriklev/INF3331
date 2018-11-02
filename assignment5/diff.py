import re
import argparse

parser = argparse.ArgumentParser(
    description="Prints the differance between the two input files.")

parser.add_argument('original', type=str,
                    help='Original-file path.')
parser.add_argument('modified', type=str,
                    help='Modified-file path.')
args = dict(parser.parse_args()._get_kwargs())
original_path, modified_path = [args[key] for key in ["original", "modified"]]

with open(original_path, 'r') as file:
    original = file.readlines()
with open(modified_path, 'r') as file:
    modified = file.readlines()

mods = {}

for i in range(len(original)):
    if modified.__contains__(original[i]):
        mods[original[i]] = ("0", i)
    else:
        mods[original[i]] = ("-", i)

for i in range(len(modified)):
    if not mods.__contains__(modified[i]):
        mods[modified[i]] = ("+", i)


def get_index(x):
    """Takes a key from the mods library, and retrives the indexvalue stored
    in the library.

    Args:
        x (string): Key from mods library.

    Returns:
        int: index of the line stored at that key
    """
    return mods[x][1]


sorted_mods = sorted(mods, key=get_index)

write_file = "diff_output.txt"
with open(write_file, 'w') as file:
    for value in sorted_mods:
        file.write(mods[value][0] + " " + value)
        print(mods[value][0], value[:-1])
