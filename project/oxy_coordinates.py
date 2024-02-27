import math
import numpy as np
from typing import List, Tuple


class OxyCoordinates():
    def __init__(self, atoms, x, y, z):
        self.atoms = atoms
        self.x = x
        self.y = y
        self.z = z

    def _calculate_r(self, i, j) -> float:
        """Distance between two points
        """
        x, y, z = self.x, self.y, self.z
        return math.sqrt(
            (x[i]-x[j])**2
            + (y[i]-y[j])**2
            + (z[i]-z[j])**2)

    def _oxy_index(self) -> List:
        """Oxygen indices
        """
        return [i for i, j in enumerate(self.atoms) if j == 'O']

    def _oxy_distances(self, i) -> List:
        """Oxygen-atom distances
        """
        distance_ro = []
        for j in range(len(self.atoms)):
            distance_ro.append(self._calculate_r(i, j))

        return distance_ro

    def _ccarbonyl_index(self, distance_ro) -> Tuple[List, np.array]:
        """C-carbonyl index
        """
        distance_so = sorted(distance_ro)
        ccarbonyl = np.argwhere(
            np.array(distance_ro) == distance_so[1]
            )[0][:].tolist()

        return ccarbonyl, distance_so

    def _ccarbonyl_distance(self, ccarbonyl, distance_so) -> List:
        """Compute distances from C-carbonyl & get closest atoms
        """
        distance_from_c = []
        for i in ccarbonyl:
            if (1.16 <= distance_so[1] <= 1.29) and (self.atoms[i] == 'C'):
                for j in range(len(self.atoms)):
                    distance_from_c.append(self._calculate_r(i, j))

        return distance_from_c

    def _pick_coordinates(self, distance_from_c) -> List:
        """Pick coordinates
        """
        c_sorted = sorted(distance_from_c)

        pick_coord = []
        for idx, distance in enumerate(distance_from_c):
            if distance == c_sorted[1]:
                pick_coord.append(idx)
            elif len(pick_coord) == 2:
                pick_coord.pop()

            if distance == c_sorted[2]:
                pick_coord.append(idx)
            elif len(pick_coord) == 3:
                pick_coord.pop()

            if distance == 0:
                pick_coord.append(idx)

        return pick_coord

    def _oxy_coords(self, pick_coord) -> List:
        """Generate new oxygen coordinates

        Order of index atoms in pick_coord must be [O, R, C]
        """
        x, y, z = self.x, self.y, self.z

        vec1 = [x[pick_coord[0]]-x[pick_coord[2]],
                y[pick_coord[0]]-y[pick_coord[2]],
                z[pick_coord[0]]-z[pick_coord[2]]]

        vec2 = [x[pick_coord[1]]-x[pick_coord[2]],
                y[pick_coord[1]]-y[pick_coord[2]],
                z[pick_coord[1]]-z[pick_coord[2]]]

        vec3 = np.cross(vec1, vec2)
        normf = np.linalg.norm(vec3)

        xO = 5.67*(1/normf)*vec3[0] + x[pick_coord[2]]
        yO = 5.67*(1/normf)*vec3[1] + y[pick_coord[2]]
        zO = 5.67*(1/normf)*vec3[2] + z[pick_coord[2]]

        return list((xO, yO, zO))

    @property
    def get_oxy_coords(self) -> List[List]:
        """All possible new oxygen coordinates
        """
        oxy_index = self._oxy_index()

        oxy_coords = []
        for i in oxy_index:
            distance_ro = self._oxy_distances(i)
            ccar, distance_so = self._ccarbonyl_index(distance_ro)
            distance_from_c = self._ccarbonyl_distanc(ccar, distance_so)
            pick_coord = self._pick_coordinates(distance_from_c)
            oxy_coords.append(self._oxy_coords(pick_coord))

        return oxy_coords
