"""
An input CSV file containing statistical information about diseases in different locations is given.

Here are the definitions of each column in the input file:

1. location_code: The unique identifier of the location
2. disease: Name of the disease
3. prevalence: Number of people having the disease
4. population: Number of people living in the location

Please complete the following Python function that:
(a) calculates the percentage of people who have each disease in each location, and
(b) writes the result to a specified CSV file

Notes:
1. If there is no information about a disease for a specific location, the percentage should be considered zero.
2. The output file should contain a column specifying the location and a column for each disease.
3. The samples of input and output files have been attached.
"""

import sys


def calculate_prevalence_rate_by_location(input_path: str, output_path: str) -> None:
    pass


if __name__ == '__main__':
    input_path = str(sys.argv[1]).strip()
    output_path = str(sys.argv[2]).strip()

    calculate_prevalence_rate_by_location(input_path, output_path)
