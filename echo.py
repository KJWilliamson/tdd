#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "kamela williamson"
# Daniel's demos for tdd and argparse
# my assessment babynames
# https://www.freecodecamp.org/news/learning-to-test-with-python-997ace2d8abe/
# https://realpython.com/python-testing/
# https://www.youtube.com/watch?v=6tNS--WetLI&feature=emb_title
# https://docs.python.org/3/library/unittest.html#module-unittest
# https://docs.python.org/3/library/unittest.html#basic-example
# https://docs.python.org/3/library/unittest.html#assert-methods
# https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
# https://docs.python.org/3/howto/argparse.html


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    # your code here. looking at babynames
    parser = argparse.ArgumentParser(description="Changes text")
    parser.add_argument("text", help="text to be changed")
    parser.add_argument("-t", "--title",
                        help="convert to titlecase",
                        action="store_true")
    parser.add_argument("-l", "--lower",
                        help="convert to lowercase",
                        action="store_true")
    parser.add_argument("-u", "--upper",
                        help="convert to uppercase",
                        action="store_true")
    return parser


def main(args):
    """Implementation of echo"""
    # your code here. got from babynames
    parser = create_parser()
    args = parser.parse_args(args)

    if not args:
        parser().print_usage()
        sys.exit(1)

    text = args.text

    if args.upper:
        text = text.upper()
    if args.lower:
        text = text.lower()
    if args.title:
        text = text.title()
    return text


if __name__ == '__main__':
    main(sys.argv[1:])
