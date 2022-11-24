import os
import argparse
from pydicom.filereader import dcmread


def main():
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('input_folder', help='Path to the folder (without spaces in the names) '
                                             'that contains only dicom folders for each sequence')
    parser.add_argument('output_folder',
                        help='Path to folder that will contain all anonymized dicom sequences\' folders')
    args = parser.parse_args()

    input_path = args.input_folder
    output_path = args.output_folder
    print(os.path.exists(input_path), os.path.exists(output_path))
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    for root, dirs, files in os.walk(input_path):
        for name in files:
            if name.endswith('.IMA') or name.endswith('.dcm'):
                input_file = os.path.join(root, name)
                input_sequence_folder = os.path.split(root)[-1]
                output_dir = os.path.join(output_path, input_sequence_folder)
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                output_file = os.path.join(output_dir, name)
                os.system(f'dicom-anonymizer "{input_file}" "{output_file}"')


if __name__ == '__main__':
    main()
