#! urs/bin/env python3 (which interpreter to use)

"""What does this Module do? This is for ....

Usage:
    python a03_module_function.py <URL>

"""

from urllib.request import urlopen
import sys

def fetch_words(url):
    """Use url to extract text online and turn into a list of strings

    Args:
        url: a single web address as string

    Returns:
        story_words: a list of strings
    """
    with urlopen(url) as story:
        story_words = [] # global variable
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words

def print_words(story_words):
    for word in story_words:
        print(word)

# global variables on the level of classes, functions

def main(url): # like C, int main(): {.....}
    # most variables to run can be defined here (local variable)
    words = fetch_words(url)
    print_words(words)

if __name__ == "__main__":
    # other global variables
    url = sys.argv[1] # sys.argv[0] == filename
    main(url)

# import a03_module_function
# from a03_module_function import (fetch_words,
# print_words)
# from a03_module_function import *
# python a03_module_function.py "http://sixty-north.com/c/t.txt"
# explore argparse module
