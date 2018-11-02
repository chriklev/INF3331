""" Script for syntax-highlighting code.
"""
import re
import argparse

parser = argparse.ArgumentParser(
    description="Highlights syntax in a given code file.")

parser.add_argument('syntax', type=str,
                    help='Syntax-file path.')
parser.add_argument('theme', type=str,
                    help='Theme-file path.')
parser.add_argument('code', type=str,
                    help='Code-file path.')
args = dict(parser.parse_args()._get_kwargs())
syntax_path, theme_path, code_path = [args[key]
                                      for key in ["syntax", "theme", "code"]]

norm = '\033[0m'

with open(code_path, 'r') as file:
    text = file.read()

with open(theme_path, 'r') as file:
    theme_text = file.read()
regex_themes = r"(.*): (\d*;\d*)"
theme_list = re.findall(regex_themes, theme_text)
themes = {key: value for (key, value) in theme_list}

with open(syntax_path, 'r') as file:
    syntax_text = file.read()
regex_syntax = r'"(.*)": (.*)'
syntax_list = re.findall(regex_syntax, syntax_text)

for synt in syntax_list:
    text = re.sub(synt[0], "\033[{}m".format(
        themes[synt[1]]) + r"\1" + norm, text)


print(text)
