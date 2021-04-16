import pandas as pd
import argparse


def create_argument_parser():
    parser  = argparse.ArgumentParser(description = 'csv-sorter: Sort a CSV file by a particular column.')
    parser.add_argument('--input-file', nargs = '?', required = False, help = 'A CSV input file.')
    #parser.add_argument('--column', nargs = '?', required = True, help = 'The column to sort CSV by.')
    #parser.add_argument('--order', nargs = '?', required = True, choices=['asc', 'dec'], help = 'Ascending or descending')
    parser.add_argument('--output-file', nargs = '?', required = False, help = 'A txt output file.')
    return parser


if __name__ == "__main__":
    parser = create_argument_parser()
    args = parser.parse_args()

    with open(args.input_file) as csv_file:
        df = pd.read_csv(csv_file)
        df = df[df['Election_Type'] == "General"]

    with open(args.output_file, mode="w") as out_file:

        with open(args.output_file, 'w') as output_file:
            output_file.writelines(df["Votes"].sum())
