import os
import gzip
from zipfile import ZipFile

def decompress_file(input_file, output_file):
    with gzip.open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        f_out.write(f_in.read())

def unzip_all_mhd_files(parent_dir, output_dir):
    for root, dirs, files in os.walk(parent_dir):
        for zip_file in [f for f in files if f.endswith('.zip')]:
            zip_file_path = os.path.join(root, zip_file)
            
            with ZipFile(zip_file_path, 'r') as zipf:
                zipf.extractall(output_dir)

            extracted_dir = os.path.join(output_dir, os.path.splitext(zip_file)[0])

            for compressed_file in os.listdir(extracted_dir):
                if compressed_file.endswith('.gz'):
                    compressed_file_path = os.path.join(extracted_dir, compressed_file)
                    decompressed_file_path = os.path.join(extracted_dir, os.path.splitext(compressed_file)[0])

                    decompress_file(compressed_file_path, decompressed_file_path)

# Example usage:
parent_directory = '/path/to/parent'
output_directory = '/path/to/output'
unzip_all_mhd_files(parent_directory, output_directory)