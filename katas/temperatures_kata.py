"""Coding Game Temperatures Kata that can be found
here: https://www.codingame.com/ide/puzzle/temperatures."""


def temperature_closest_to_zero(temperatures):
    """Receives an array of temperatures and returns the closest one to zero"""

    closest_to_zero = temperatures[0]
    for temperature in temperatures:
        if (abs(temperature) < abs(closest_to_zero) or
                (abs(temperature) == abs(closest_to_zero) and temperature > 0)):
            closest_to_zero = temperature

    return closest_to_zero


def main():
    """Receives the number of temperatures to capture (number_of_temperatures)
    and the temperatures."""

    number_of_temperatures = int(input())
    temperatures_input = []
    for i in input().split():
        temperatures_input.append(int(i))

    if number_of_temperatures == 0:
        result = 0
    else:
        result = temperature_closest_to_zero(
            [int(t) for t in temperatures_input])

    print(result)


if __name__ == "__main__":
    main()
