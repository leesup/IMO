#!/usr/bin/env python3

# Genomics analysis wrapper file

# Import Python dependencies
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Wrapper for running genomics analysis scripts.")
    
    # Define the command-line arguments with short versions
    parser.add_argument(
        '-p', '--path',
        type=str,
        required=True,
        help='Path to the directory or file for the genomics analysis'
    )
    
    parser.add_argument(
        '-f', '--file_format',
        type=str,
        choices=['csv', 'tsv', 'json'],  # Add more formats if needed
        default='csv',
        help='File format of the input data (default: csv)'
    )
    
    parser.add_argument(
        '-r', '--reference_genome',
        type=str,
        required=True,
        help='Path to the reference genome file'
    )
    
    return parser.parse_args()

def main():
    args = parse_arguments()
    
    # Use the parsed arguments
    print(f"Path: {args.path}")
    print(f"File Format: {args.file_format}")
    print(f"Reference Genome: {args.reference_genome}")
    
    # Pass arguments to your analysis function or script
    run_analysis(args.path, args.file_format, args.reference_genome)

def run_analysis(path, file_format, reference_genome):
    # Replace with the actual function or script logic
    print(f"Running analysis with the following parameters:")
    print(f"  Path: {path}")
    print(f"  File Format: {file_format}")
    print(f"  Reference Genome: {reference_genome}")

if __name__ == "__main__":
    main()

