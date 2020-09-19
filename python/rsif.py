#!/usr/bin/env python3
"""
Replace String in Filename
"""
import sys
import os


def main(argv):
    length = len(argv)
    if length < 2:
        print(
            "usage (replace string in filename with new string): rsif [dir or filename] [old_string] [new_string]"
        )
        sys.exit()
    elif length == 2:
        argv.append('')

    input_path = argv[0]
    old_string = argv[1]
    new_string = argv[2]

    # the input param is a single file
    if os.path.isfile(input_path):
        os.rename(input_path, input_path.replace(old_string, new_string))

    # the input is a dir
    elif os.path.isdir(input_path):
        for filename in os.listdir(input_path):
            os.rename(filename, filename.replace(old_string, new_string))

    else:
        print("not a valid file or dir.")
        sys.exit()


if __name__ == "__main__":
    main(sys.argv[1:])
