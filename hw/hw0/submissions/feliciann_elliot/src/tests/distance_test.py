from .. import tokenization
from tokenization import edit_distance

def main():
    print(edit_distance("kitten", "sitting"))  # Output: 3
    print(edit_distance("saturday", "sunday"))  # Output: 3

if __name__ == "__main__":
    main()