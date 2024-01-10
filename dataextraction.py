import os
import gzip
from zipfile import ZipFile

def decompress_file(input_file, output_file):
    with gzip.open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        f_out.write(f_in.read())

def unzip_and_decompressed(parent_dir, output_dir):
    for root, dirs, files in os.walk(parent_dir):
        for zip_file in [f for f in files if f.endswith('.zip')]:
            zip_file_path = os.path.join(root, zip_file)
            zip_name = os.path.splitext(zip_file)[0]
            extracted_dir = os.path.join(output_dir, zip_name)

            with ZipFile(zip_file_path, 'r') as zipf:
                zipf.extractall(extracted_dir)

            for gz_file in os.listdir(extracted_dir):
                gz_file_path = os.path.join(extracted_dir, gz_file)

                if gz_file.endswith('_raw.gz'):
                    original_file_path = os.path.join(extracted_dir, zip_name + '.raw')
                elif gz_file.endswith('_mhd.gz'):
                    original_file_path = os.path.join(extracted_dir, zip_name + '.mhd')

                decompress_file(gz_file_path, original_file_path)
                os.remove(gz_file_path)

# Example usage:
parent_directory = 'Y:\\aorta_data\\PLOS2024\\zipped_and_compressed'
output_directory = 'Y:\\aorta_data\\PLOS2024\\unzipped_and_decompressed'
unzip_and_decompressed(parent_directory, output_directory)