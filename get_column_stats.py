import sys
import math
import argparse as ap


# Function to calculate the mean of a integer vector
def calcMean(val):
    if val is None:
        raise TypeError("calcMean: Empty input")
        sys.exist(1)
    return (sum(val)/len(val))


# Function to calculate the stdard deviation of a integer vector
def calcStdev(val):
    if val is None:
        raise TypeError("calcStdev: Empty input")
        sys.exist(1)
    mean = calcMean(val)
    return math.sqrt(sum([(mean-x)**2 for x in val]) / len(val))


# Parsing arguments using argparse
def parseArgs():
    parser = ap.ArgumentParser(description="Process filename and columns",
                               prog='get_column_stats')

    parser.add_argument('-i',
                        '--input',
                        type=str,
                        help="Input file name",
                        required=True)

    parser.add_argument('-c',
                        '--column',
                        type=int,
                        help="Number of columns in the input file",
                        required=True)

    return parser.parse_args()


# Main
def main():
    args = parseArgs()
    filename = args.input
    # Fix the 0 based indexing in python, so the colu
    ncol = args.column - 1

    f = None
    mean = None
    stdev = None
    V = []

    # Check if the input file is valid
    try:
        inputFile = open(args.input, 'r')
    except FileNotFoundError:
        print("The specified input file does not exist. Exiting.")
        sys.exit(1)

    # Check if the input column number is valid
    if ncol < 0:
        raise ValueError('Column number must be greater than 0.')
        sys.exit(1)

    # Append a new vector with the numbers in the specified column
    for row in inputFile:
        try:
            A = [int(x) for x in row.split()]
            V.append(A[ncol])
        except ValueError:
            print('Input file contains bad formatting please check.')
            sys.exit(1)

    # Check if the previous operation is completed successfully
    if len(V) == 0:
        raise Exception('None of the values are valid for calculation')
    else:
        mean = calcMean(V)
        stdev = calcStdev(V)

    # Return the results
    print('mean:', mean)
    print('stdev:', stdev)


if __name__ == "__main__":
    main()
