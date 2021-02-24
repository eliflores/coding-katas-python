"""Half Pyramid of Numbers is a kata found in the wild.
Given a number N, print a pyramid of numbers like in the following example:
Given that N = 6, then what would be printed is:

1
1 2 1
1 2 3 2 1
1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
1 2 3 4 5 6 5 4 3 2 1
"""

import sys


def levels_content(number_of_levels):
    """Returns the contents of each pyramid level, given an N number of levels."""
    levels = []
    for level in range(1, number_of_levels + 1):
        level_content = '1'
        for number in range(2, level + 1):
            level_content += f" {number}"
        for number in reversed(range(1, level)):
            level_content += f" {number}"
        levels.append(level_content)

    return levels


def main():
    """Receives the number of levels (N) of the pyramid to print."""

    if len(sys.argv) < 2:
        print('Usage: pyramid_of_numbers_kata.py <number_of_levels>.')
        sys.exit(1)

    if not sys.argv[1].isnumeric():
        print('Usage: pyramid_of_numbers_kata.py <number_of_levels>,'
              ' where number_of_levels is a positive int.')
        sys.exit(1)

    number_of_levels = int(sys.argv[1])
    for level_content in levels_content(number_of_levels):
        print(level_content)


if __name__ == "__main__":
    main()
