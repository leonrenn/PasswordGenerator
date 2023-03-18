"""
Building the parser for the main program.
"""
from argparse import ArgumentParser


def build_parser() -> ArgumentParser:
    """Build parser for the main program.
    Returns:
        ArgumentParser: Parser.
    """
    # initialize parser class
    parser: ArgumentParser = ArgumentParser()

    # add arguments to the parser
    parser.add_argument("-n",
                        "--number_of_characters",
                        type=int,
                        default=12,
                        required=False,
                        help="Number of characters.")
    parser.add_argument("-a",
                        "--all",
                        required=False,
                        action="store_true",
                        help="All characters (alphabetic)"
                        "numeric, special).")
    parser.add_argument("-abc",
                        "--alphabetic",
                        required=False,
                        action="store_true",
                        help="Alphabetic characters.")
    parser.add_argument("-num",
                        "--numeric",
                        required=False,
                        action="store_true",
                        help="Numeric characters.")
    parser.add_argument("-s",
                        "--special",
                        required=False,
                        action="store_true",
                        help="Special characters.")

    return parser
