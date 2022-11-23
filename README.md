# Dicom-anonymization
Creates anonymized dicom files using command line and python
# Requirements
Python 3.7

pydicom

dicom-anonymizer (needs to be built, taken from: https://github.com/KitwareMedical/dicom-anonymizer)

# Installation
1. Create a virtual environment with python 3.7

2. pip install pydicom

3. For installing dicom-anonymizer:
    -   First cd to the repo directory
    -   run pip install ./dicom-anonymizer/dist/dicom_anonymizer-1.0.9-py2.py3-none-any.whl

# Usage
1. Activate the virtual environment in terminal

2. cd to the repo directory

3. run **python main.py [input_folder_path] [output_folder_path]**

    - The input_folder_path should contain all subfolders that hold all images for each sequence. The path name should ideally have no spaces in them.

    - The output_folder_path can be any folder where all anonymized files corresponding to single patient are stored.
