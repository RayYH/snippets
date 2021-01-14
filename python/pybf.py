#!/usr/bin/env python3

import sys
import os


def get_char():
    return input('').split(" ")[0]


def evaluate(commands):
    commands = normalize(commands)
    brace_map = build_brace_map(commands)
    cells = [0 * 30000]
    data_ptr = 0
    instruction_ptr = 0
    length = len(commands)

    # increment the data pointer (to point to the next cell to the right).
    def greater_than_symbol():
        nonlocal data_ptr, cells
        data_ptr += 1
        if data_ptr == len(cells):
            cells.append(0)

    # decrement the data pointer (to point to the next cell to the left).
    def less_than_symbol():
        nonlocal data_ptr, cells
        data_ptr = 0 if data_ptr <= 0 else data_ptr - 1

    # increment (increase by one) the byte at the data pointer.
    def plus_symbol():
        nonlocal data_ptr, cells
        cells[data_ptr] = cells[data_ptr] + 1 \
            if cells[data_ptr] < 255 else 0

    # decrement (decrease by one) the byte at the data pointer.
    def minus_symbol():
        nonlocal data_ptr, cells
        cells[data_ptr] = \
            cells[data_ptr] - 1 if cells[data_ptr] > 0 else 255

    # output the byte at the data pointer.
    def dot_symbol():
        nonlocal data_ptr, cells
        sys.stdout.write(chr(cells[data_ptr]))

    # accept one byte of input,
    # storing its value in the byte at the data pointer.
    def comma_symbol():
        nonlocal data_ptr, cells
        ch = get_char()
        cells[data_ptr] = ord(ch)

    # if the byte at the data pointer is zero, then instead of moving the
    # instruction pointer forward to the next command, jump it forward
    # to the command after the matching ] command.
    def left_bracket():
        nonlocal data_ptr, cells, instruction_ptr
        if cells[data_ptr] == 0:
            instruction_ptr = brace_map[instruction_ptr]

    # if the byte at the data pointer is nonzero, then instead of moving the
    # instruction pointer forward to the next command, jump it back to
    # the command after the matching [ command.
    def right_bracket():
        nonlocal data_ptr, cells, instruction_ptr
        if cells[data_ptr] != 0:
            instruction_ptr = brace_map[instruction_ptr]

    handlers = {
        '>': greater_than_symbol,
        '<': less_than_symbol,
        '+': plus_symbol,
        '-': minus_symbol,
        '.': dot_symbol,
        ',': comma_symbol,
        '[': left_bracket,
        ']': right_bracket,
    }

    while instruction_ptr < length:
        command = commands[instruction_ptr]
        handlers[command]()
        instruction_ptr += 1


def normalize(commands):
    return [
        command for command in commands
        if command in ['.', ',', '[', ']', '<', '>', '+', '-']
    ]


def run(scripts):
    if os.path.isfile(scripts):
        with open(scripts, mode="r", encoding="utf-8") as f:
            scripts = f.readlines()[0]
    evaluate(scripts)


def build_brace_map(code):
    stack, brace_map = [], {}

    for position, command in enumerate(code):
        if command == "[":
            stack.append(position)
        if command == "]":
            if len(stack) > 0:
                start = stack.pop()
                brace_map[start] = position
                brace_map[position] = start
            else:
                print("Error: missing [\n")
                sys.exit(1)
    if len(stack) > 0:
        print("Error: missing ]\n")
        sys.exit(1)
    return brace_map


def main():
    if len(sys.argv) == 2:
        run(sys.argv[1])
    else:
        print("Usage:", sys.argv[0], "<filename or code lines>")
        sys.exit()


if __name__ == '__main__':
    main()
