"""Divise un nombre pair et transmet le résultat à l'étape suivante.

Usage : python scripts/divide.py <nombre> <diviseur>
"""
import os
import sys


def parse(value):
    number = float(value)
    return int(number) if number.is_integer() else number


def main():
    number = parse(sys.argv[1])
    divisor = int(sys.argv[2])

    if not isinstance(number, int) or number % 2 != 0:
        print(f"::error::{number} est impair, arrêt de la pipeline.")
        sys.exit(1)

    result = number // divisor if number % divisor == 0 else number / divisor
    print(f"{number} / {divisor} = {result}")

    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with open(output, "a") as f:
            f.write(f"resultat={result}\n")


if __name__ == "__main__":
    main()
