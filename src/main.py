"""
Short script to generate random but secure passwords.
"""

import random
from utils.parsing import build_parser
from argparse import ArgumentParser
from typing import Dict, List, Tuple
from exceptions.parser_exceptions import (
    NoPasswordSpecification, WrongFromatParserArgument)


# MAIN


def main() -> int:

    # build parser with dedicated function
    parser: ArgumentParser = build_parser()

    # check the input arguments
    parser_dict: Dict[str, str] = vars(parser.parse_args())

    try:
        # extract the number of characters
        num_characters: int = parser_dict["number_of_characters"]
        if num_characters < 0:
            raise WrongFromatParserArgument
    except WrongFromatParserArgument:
        print("\nThe number of characters argument is not valid. Exit.")
        return -1

    # character indices
    character_selection: List[Tuple[int]] = []
    characters: List[str] = []

    # numeric indices
    numeric_indices: Tuple[int] = (48, 57)

    # capital alphabetic indices
    cap_alphabetic_indices: Tuple[int] = (65, 90)

    # lower alphabetic indices
    alphabetic_indices: Tuple[int] = (97, 122)

    # special indices
    spec_indices_0: Tuple[int] = (32, 47)
    spec_indices_1: Tuple[int] = (58, 64)

    # add indices to list dependent on arguments set via CLI parser

    try:
        if (parser_dict["numeric"] is not True and
                parser_dict["alphabetic"] is not True and
                parser_dict["special"] is not True and
                parser_dict["all"] is not True):
            raise NoPasswordSpecification
    except NoPasswordSpecification:
        print("\nNo specifiers were given but at "
              "least one is required. Exit")
        return -1

    # add numeric characters
    if (parser_dict["numeric"] is True or
            parser_dict["all"] is True):
        character_selection.append(numeric_indices)

    # add alphabetic characters
    if (parser_dict["alphabetic"] is True or
            parser_dict["all"] is True):
        character_selection.append(alphabetic_indices)
        character_selection.append(cap_alphabetic_indices)

    # add special characters
    if (parser_dict["special"] is True or
            parser_dict["all"] is True):
        character_selection.append(spec_indices_0)
        character_selection.append(spec_indices_1)

    # loop over all tuples to get a list of
    # characters that should build up the password
    for indices_tuples in character_selection:
        characters += [chr(idx) for idx in range(indices_tuples[0],
                                                 indices_tuples[1]+1)]

    # generate the password
    password = "".join(random.choices(
        population=characters, k=num_characters))

    # print the password on the CLI
    print("\nGenerated password is:\t ", password)

    return 0


# START PROGRAM

if __name__ == "__main__":
    main()
