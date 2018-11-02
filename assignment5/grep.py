import argparse
import re

parser = argparse.ArgumentParser(
    description="Searches for python regular expressions in a text")

parser.add_argument('input', type=str,
                    help='Input file path.')
parser.add_argument('regex', action='append', nargs='+', type=str,
                    help='The regular expressions to be searched for.')
parser.add_argument('--highlight', action="store_true",
                    help='Highlights the searched for text.')

args = parser.parse_args()

highlight, infile, regexes = [x[1] for x in args._get_kwargs()]

with open(infile, 'r') as file:
    text_lines = file.readlines()

for line in text_lines:
    printline = False
    for regex in regexes[0]:
        if highlight:
            line, i = re.subn(regex, "\033[7m" + r"\1" + "\033[0m", line)
            if i > 0:
                printline = True
        elif re.search(regex, line) is not None:
            printline = True
    if printline:
        print(line[:-1])
