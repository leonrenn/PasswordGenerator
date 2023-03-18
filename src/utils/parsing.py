"""
Building the parser for the main program.
"""
from argparse import ArgumentParser


def build_parser() -> ArgumentParser:
    """Build parser for the main program.
    Returns:
        ArgumentParser: Parser.
    """
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument("-r",
                        "--root",
                        type=str, required=False,
                        help=".root files as input from "
                        "SimpleAnalysis Tool.")

    parser.add_argument("-d",
                        "--droot",
                        type=str,
                        required=False,
                        help="Directory with .root files"
                        " from SimpleAnalysis Tool.")
    parser.add_argument("-t",
                        "--threshold",
                        type=float,
                        required=False,
                        help="Threshold for "
                        "generating binary "
                        "correlation matrix.")
    parser.add_argument("-nw",
                        "--no_weights",
                        required=False,
                        action="store_true",
                        help="Force that all signal regions"
                        " are treated equally in "
                        "significance.")
    parser.add_argument("-np",
                        "--no_plots",
                        required=False,
                        action="store_true",
                        help="No plots are saved in the"
                        " result dir.")
    parser.add_argument("-tp",
                        "--top_paths",
                        type=int,
                        required=False,
                        help="Number of top paths"
                        " printed on CLI and saved"
                        " in result dir")
    parser.add_argument("-st",
                        "--statistics",
                        required=False,
                        action="store_true",
                        help="Raise errors when not"
                        "having collected enough statistics.\n"
                        "Makes program much slower.")
    parser.add_argument("-cm",
                        "--corr_matrix",
                        required=False,
                        type=str,
                        help="The correlation matrix is "
                        "given as an input file to the "
                        "program.")
    parser.add_argument("-ps",
                        "--preselecting",
                        required=False,
                        type=str,
                        help="Preselecting SR based on info "
                        "files of given directory.")
    parser.add_argument("-ht",
                        "--histogram",
                        required=False,
                        action="store_true",
                        help="Plot a histogram for number of "
                        "events per signal region.")
    parser.add_argument("-ccm",
                        "--cross_check_matrices",
                        required=False,
                        action="store_true",
                        help="Plot cross check matrices for"
                        " validating the overlap of SRs.")
    return parser
