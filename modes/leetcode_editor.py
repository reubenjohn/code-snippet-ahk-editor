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


def process(input_file: typing.IO, output: typing.IO, name: str):
    lines = input_file.readlines()

    output.write(f"""#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
#SingleInstance Force
SendMode Event  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

get_code_snippet_{name}()
{{
""")

    keys = []

    def add_key(key: str):
        keys.append(f'"{key}"')

    for curr, nxt in zip_line_pairs(lines):
        if curr == '\n':
            add_key("{Enter}")
            continue

        curr_stripped = curr.strip()
        nxt_stripped = (nxt or '').strip()
        if len(curr_stripped) == 0: continue
        for c in curr_stripped:
            if c == ' ':
                add_key('{Space}')
            elif c == '}':
                add_key('{Down}{End}')
            elif c == '"':
                add_key('""')
            else:
                add_key(f"{{{c}}}")

        if nxt is not None and not nxt_stripped.startswith('}'):
            add_key("{Enter}")

    partition_size = 10
    arrays = [keys[i:i + partition_size] for i in range(len(keys))[::partition_size]]
    concatenations = "\n".join([f"    arr.push([{', '.join(arr)}]*)" for (idx, arr) in enumerate(arrays)])

    output.write(f"""    arr := []
{concatenations}
    Return arr
}}
""")
