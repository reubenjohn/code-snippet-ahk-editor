import os
import random
import typing

MODE_IDENTIFIER = 'leetcode-editor'


def process(input_file: typing.IO, output: typing.IO, shortcut: str):
    lines = input_file.readlines()

    output.write(f"""#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Event  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

{shortcut}::GoTo, CMD

CMD:
""")

    for line in lines:
        stripped = line.strip()
        if len(stripped) == 0: continue
        for c in stripped:
            if c == ' ':
                c = 'Space'
            output.write(f'Sleep, {int(random.normalvariate(311, 152))}{os.linesep}')
            output.write(f'Send, {{{c}}}{os.linesep}')
        output.write(f'Send, {{Enter}}{os.linesep}')

    output.write("""
return

""")