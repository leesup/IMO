#!/usr/bin/env python3

# Load genomics data

# Import Python dependencies
import argparse
import hail as hl

def load_data(path, file_format, reference_genome):
    hl.init()  # Initialize Hail
    
    if file_format == 'vcf':
        # Load VCF file
        print(f"Importing VCF file from {path}")
        mt = hl.import_vcf(path, reference_genome=reference_genome)
        print(f"Loaded VCF file: {mt.count()} rows")
        
    elif file_format == 'plink':
        # Load PLINK files
        print(f"Importing PLINK files from {path}")
        mt = hl.import_plink(bed=path + '.bed', bim=path + '.bim', fam=path + '.fam', reference_genome=reference_genome)
        print(f"Loaded PLINK files: {mt.count()} rows")
        
    else:
        raise ValueError(f"Unsupported file format: {file_format}")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Load files with specified parameters.")
    
    parser.add_argument(
        '--path',
        type=str,
        required=True,
        help='Path to the directory or file for the analysis'
    )
    
    parser.add_argument(
        '--file_format',
        type=str,
        choices=['vcf', 'plink'],  # Supported formats
        required=True,
        help='File format of the input data'
    )
    
    parser.add_argument(
        '--reference_genome',
        type=str,
        required=True,
        help='Path to the reference genome file'
    )
    
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    load_data(args.path, args.file_format, args.reference_genome)





