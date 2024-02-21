import pandas as pd

class Molecule:
    def __init__(self, file_name):
        self.file_name = file_name
    
    
    #extract coordinates as pandas data frame
    def get_coordinates(self):
        with open(self.file_name) as file:
            n_atoms = int(file.read().split()[0])
        with open(self.file_name) as file:
            lines = file.read().split()[2:]

        print(n_atoms)
        
        atoms = []
        x = []
        y = []
        z = []

        for i in range(n_atoms):
            atoms.append(lines[i*4])
            x.append(float(lines[(i*4+1)]))
            y.append(float(lines[(i*4+2)]))
            z.append(float(lines[(i*4+3)]))

            coordinates = pd.DataFrame(list(zip(atoms,x,y,z)))
        return(coordinates)

test1 = Molecule('mol_test.xyz')
test1.get_coordinates()