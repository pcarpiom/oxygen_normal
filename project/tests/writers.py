import pandas as pd
import logging

logger = logging.getLogger('Insert oxygen')


class Molecule:
    """Parse .xyz file
    """
    def __init__(self, file_name):
        self.file_name = file_name

    @property
    def coordinates(self):
        """Get (x, y, z) coordinates

        :return: pd.DataFrame
        """
        with open(self.file_name) as file:
            file = file.read().split()
            n_atoms = int(file[0])
            lines = file[2:]

        logger.info(n_atoms)

        atoms = []
        x = []
        y = []
        z = []

        for i in range(n_atoms):
            atoms.append(lines[i*4])
            x.append(float(lines[(i*4+1)]))
            y.append(float(lines[(i*4+2)]))
            z.append(float(lines[(i*4+3)]))

        columns = ['atom', 'x', 'y', 'z']
        coord = pd.DataFrame(list(zip(atoms, x, y, z)), columns=columns)

        logger.info(coord)

        return coord
