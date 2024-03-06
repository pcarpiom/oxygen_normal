import sys
sys.path.append('./project/')

import glob
from pathlib import Path
from typing import List
import argparse
from writers import *
from oxy_coordinates import *

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

for file in outfiles:
    test = Molecule(file)
    testc = OxyCoordinates(test.coordinates['atom'].tolist(), 
                           test.coordinates['x'].tolist(), 
                           test.coordinates['y'].tolist(), 
                           test.coordinates['z'].tolist())
    test.writefile(testc.get_oxy_coords)
