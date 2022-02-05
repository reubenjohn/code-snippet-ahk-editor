#!/usr/bin/python
import sys, getopt
from pathlib import Path

from modes import leetcode_editor


def print_help():
    print('test.py -i <inputfile> -o <outputfile> -m <mode> -k <autohotkey-keyboard-shortcut>', file=sys.stderr)
    print('Supported <mode>: leetcode-editor', file=sys.stderr)


def main(argv):
    input_path = output_path = mode = shortcut = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:m:k:", ["ifile=", "ofile=", "mode=", "keyboard-shortcut="])
        if any((arg not in [opt[0] for opt in opts]) for arg in ['-i', '-o', '-m']):
            raise getopt.GetoptError('Missing argument')
    except getopt.GetoptError:
        print_help()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_path = Path(arg)
        elif opt in ("-o", "--ofile"):
            output_path = Path(arg)
        elif opt in ("-m", "--mode"):
            mode = arg
        elif opt in ("-k", "--keyboard-shortcut"):
            shortcut = arg

    print(f'Input file: "{input_path}"')
    print(f'Output file: "{output_path}"')
    print(f'Mode: "{mode}"')
    print(f'Shortcut: "{shortcut}"')

    if mode == leetcode_editor.MODE_IDENTIFIER:
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(input_path) as input_file:
            with open(output_path, "w") as output_file:
                leetcode_editor.process(input_file, output_file)


if __name__ == "__main__":
    main(sys.argv[1:])
