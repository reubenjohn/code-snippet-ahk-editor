import os
import random
import typing

MODE_IDENTIFIER = 'leetcode-editor'

mean, std = 311, 152
mean //= 16
std //= 16

def process(input_file: typing.IO, output: typing.IO, shortcut: str):
    lines = input_file.readlines()

    output.write(f"""#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
#SingleInstance Force
SendMode Event  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

Escape::Reload
{shortcut}::GoTo, CMD

CMD:
""")

    for line in lines:
        stripped = line.strip()
        if len(stripped) == 0: continue
        for c in stripped:
            if c == ' ':
                c = 'Space'
            elif c == '}':
                c = 'Down'

            output.write(f'Sleep, {int(random.normalvariate(mean, std))}{os.linesep}')
            output.write(f'Send, {{{c}}}{os.linesep}')
        output.write(f'Send, {{Enter}}{os.linesep}')

    output.write("""
return

""")
