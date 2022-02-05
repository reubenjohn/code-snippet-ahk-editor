import typing

MODE_IDENTIFIER = 'leetcode-editor'


def process(input_file: typing.IO, output_file):
    content = "\n".join(input_file.readlines())
    print(f"Input code snippet:\n{content}")
    output_file.write(content)