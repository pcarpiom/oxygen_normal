import glob
from pathlib import Path
from typing import List
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('WORKDIR', help='enter WORKDIR')
parser
args = parser.parse_args()

FILES_PATH = args.WORKDIR + '*.xyz'


def get_outfiles(DIR: str) -> List:
    """Get filepaths
    """

    file_paths = glob.glob(DIR, recursive=True)

    return file_paths


outfiles = get_outfiles(FILES_PATH)
for file in outfiles:
    print(Path(file))