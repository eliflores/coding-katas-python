"""Coding Game Temperatures Kata that can be found
here: https://www.codingame.com/ide/puzzle/temperatures."""


def temperature_closest_to_zero(temperatures):
    """Receives an array of temperatures and returns the closest one to zero"""

    closest_to_zero = temperatures[0]
    for temperature in temperatures:
        if temperature > 0:
            if temperature < closest_to_zero or abs(closest_to_zero) == temperature:
                closest_to_zero = temperature
        elif temperature < 0:
            if temperature > closest_to_zero:
                closest_to_zero = temperature
        else:
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
        result = temperature_closest_to_zero([int(t) for t in temperatures_input])

    print(result)


if __name__ == "__main__":
    main()
