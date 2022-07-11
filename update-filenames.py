from ast import Store
import shutil
import sys
import os
import argparse
from pathlib import Path
from argparse import RawTextHelpFormatter
import textwrap


BASE_DIR = os.getcwd()
files_to_modify = os.listdir(BASE_DIR)

# for file in files_to_modify:
#     new_name = file.replace(' .png', '.png')
#     new_name = new_name.split('. ')[1]
#     shutil.move(BASE_DIR+file, BASE_DIR+new_name)


def to_lowercase():
    """
    It takes all the files in the directory and converts them to lowercase
    """
    files_to_modify = os.listdir(BASE_DIR)
    for file in files_to_modify:
        new_name = file.lower()
        shutil.move(BASE_DIR+file, BASE_DIR+new_name)


def to_uppercase():
    """
    It takes all the files in the directory, converts them to uppercase.
    """
    files_to_modify = os.listdir(BASE_DIR)
    for file in files_to_modify:
        new_name = file.upper()
        shutil.move(BASE_DIR+file, BASE_DIR+new_name)


def init_argparse():
    """
    It creates an argument parser that can be used to parse the command line arguments
    :return: The parser object is being returned.
    """
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION] [FILE]...",
        description="Updates all files in the provided directory",
        formatter_class=argparse.RawTextHelpFormatter
    )

    transformation = parser.add_mutually_exclusive_group()
    transformation.add_argument("-l", "--lowercase", action='store_true',
        help="Renames all matching files to lowercase format")
    transformation.add_argument("-u", "--uppercase", action='store_true',
        help="Renames all matching files to uppercase format")

    parser.add_argument('-p', '--pattern', nargs='?', default='*',
        help=textwrap.dedent('''\
        Sets the pattern used to filter files to rename.
            - *     Match everything except slashes
            - **    Recursively matches zero or more directories that fall under the current directory.
            - ?     Match any single character.
                    For example to match any three-letter filename that ends in \"at\", you could use the pattern \"?at\"
                    This will return files named like:
                        * Cat
                        * Bat
                        * cat
                        * and so on.
            - [ABC] Denotes a pattern that should match a single character. This type of pattern
                    is called \'Character classes\'. Please note that the string inside of the brackets
                    is not allowed to be empty, this could lead to unexpected behavior.
                    The pattern \"[CBR]\" will return files named like:
                        * Cat
                        * Bat
                        * Rat
                        * and so on.
                    Note that it is case-sensitive, so file like \'cat\' or \'rat\', will not be returned.
                    If said files should be returned, include those characters into the character class,
                    like \'[CBRcbr]\'
            - [A-E] Ranges match any single character between the specified range. For example:
                        * [A-Z] All uppercase letters from A to Z
                        * [a-z] All lowercase letters from a to z
                        * [0-9] All numbers from 0 to 9

        '''))

    parser.add_argument('dir', default=BASE_DIR, nargs="?")
    return parser


# A way to make sure that the code is only executed when the file is run directly.
if __name__ == "__main__":
    parser = init_argparse()
    args = parser.parse_args()
    if 'dir' in args:
        BASE_DIR = os.path.abspath(args.dir)
    parser.print_help()
    print(args)
    # if args.lowercase:
    #     to_lowercase()
    # if args.uppercase:
    #     to_uppercase()
    # if not args.files:
    #     output_sha1sum(process_stdin())
    # for file in args.files:
    #     if file == "-":
    #         output_sha1sum(process_stdin(), "-")
    #         continue
    #     try:
    #         output_sha1sum(process_file(file), file)
    #     except (FileNotFoundError, IsADirectoryError) as err:
    #         print(f"{sys.argv[0]}: {file}: {err.strerror}", file=sys.stderr)

    # rename_file()
