import os
import random
import typing

MODE_IDENTIFIER = 'leetcode-editor'

mean, std = 311, 152
mean //= 16
std //= 16


def zip_line_pairs(lines: [str]):
    prev = None
    for line in lines:
        if prev is not None:
            yield prev, line
        prev = line
    yield prev, None


def process(input_file: typing.IO, output: typing.IO, shortcut: str):
    lines = input_file.readlines()

    output.write(f"""#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
#SingleInstance Force
SendMode Event  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

rand_gaussian(mean, standard_deviation)
{{
	max_random = 10000000
	Random, r1, 1, max_random ; 1 to prevent inf error
	Random, r2, 1, max_random
	Return mean + standard_deviation * Sqrt(-2 * Ln(r1 / max_random)) * Cos(2 * 3.14159265 * (r2 / max_random))
}}

Escape::GoTo, OnStop
RCtrl & `::GoTo, MatchShortcut

MatchShortcut:
Input userKeys, L2
if (userKeys == "{shortcut}") {{
	GoTo, CMD
}} else {{
	Reload
}}

return

OnStop:
Send, {{Shift Up}}
Send, {{Ctrl Up}}
Send, {{Alt Up}}
Reload
return

CMD:
""")

    for curr, nxt in zip_line_pairs(lines):
        if curr == '\n':
            output.write(f'Send, {{Enter}}{os.linesep}')
            continue

        curr_stripped = curr.strip()
        nxt_stripped = (nxt or '').strip()
        if len(curr_stripped) == 0: continue
        for c in curr_stripped:
            if c == ' ':
                delay_and_type(output, '{Space}')
            elif c == '}':
                delay_and_type(output, '{Down}{End}')
            else:
                delay_and_type(output, f"{{{c}}}")

        if nxt is not None and not nxt_stripped.startswith('}'):
            output.write(f'Send, {{Enter}}{os.linesep}')

    output.write("""
return

""")


def delay_and_type(output: typing.IO, key: str):
    output.write(f'Sleep, rand_gaussian(mean, std){os.linesep}')
    output.write(f'Send, {key}{os.linesep}')
