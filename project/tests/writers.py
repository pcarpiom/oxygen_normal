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
            self.n_atoms = int(file[0])
            lines = file[2:]

        logger.info(self.n_atoms)

        atoms = []
        x = []
        y = []
        z = []

        for i in range(self.n_atoms):
            atoms.append(lines[i*4])
            x.append(float(lines[(i*4+1)]))
            y.append(float(lines[(i*4+2)]))
            z.append(float(lines[(i*4+3)]))

        columns = ['atom', 'x', 'y', 'z']
        coord = pd.DataFrame(list(zip(atoms, x, y, z)), columns=columns)

        logger.info(coord)

        return coord

    def writefile(self, oxygen_coordinates):
        """print out xyz file with new O atoms

        """
        
        update_atoms = self.n_atoms + len(oxygen_coordinates)

        #xyz format 
        with open(self.file_name.replace('.xyz', '_oxy.xyz'), 'w') as nf:
            print(update_atoms, file=nf)
            print('mol', file=nf)
            print(self.coordinates.to_string(index=False, header=False), file=nf)
            for i in range(2):
                str_oxy_coords = 'O  %.6f  %.6f  %.6f ' % ( oxygen_coordinates[i][0], 
                                                           oxygen_coordinates[i][2], 
                                                           oxygen_coordinates[i][1])
                print(str_oxy_coords, file=nf)
