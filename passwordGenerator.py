"""
Short script to generate random but secure passwords
"""

# MODULES
import random

def main() -> None:
    while True:
        try:
            numberOfCharacters = int(input("How many characters?"))
            break
        except Exception:
            print("Provide a valid argument!\n")
    characters = [chr(i) for i in range(33,127)] # beginning with !
    pwd = [random.choice(characters) for _ in range(numberOfCharacters)]
    print("".join(pwd))
    return

if __name__ == "__main__":
    main()
