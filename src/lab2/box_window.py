from lab2.utils import get_random_number_generator
import numpy as np


class BoxWindow:
    """BoxWindow is a cube of N dimensions."""

    def __init__(self, bounds):
        """initialization of the box

        Args:
            bounds (array): array of ranges of the box in all the directions of the space.
        """

        self.bounds = bounds

    def __str__(self):
        r"""BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            [string]: Written representation of the box with its bounds.
        """
        string = "BoxWindow: "
        dim = self.dimension()
        i = 0

        for list in self.bounds:

            a = list[0]
            b = list[1]
            if a.dtype == "float64" and a.is_integer():
                a = int(a)
            if b.dtype == "float64" and b.is_integer():
                b = int(b)

            if i == dim - 1:
                string += "[" + str(a) + ", " + str(b) + "]"

            else:
                string += "[" + str(a) + ", " + str(b) + "]" + " x "
            i += 1

        return string

    def __len__(self):
        """returns the length of the longest side of the box"""
        return np.max(np.array([b - a for [a, b] in self.bounds]))

    def __contains__(self, point):
        """Returns true if a point is contained in the box.

        Args:
            point (array): Coordinates of the point
        """
        assert len(point) == self.dimension()
        bounds = self.bounds
        dim = self.dimension()
        for i in range(dim):
            if not bounds[i][0] <= point[i] <= bounds[i][1]:
                return False

        return True

    def dimension(self):
        """Returns the number of dimensions of the box"""
        return len(self.bounds)

    def volume(self):
        """Returns the volume of the box"""
        V = 1
        for [a, b] in self.bounds:
            V *= b - a
        return V

    def indicator_function(self, point):
        """Tests if a point is in the box

        Args:
            point (array): Coordinates of the point
        """

        return point in self

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.
        """

        rng = get_random_number_generator(rng)
        pointArray = np.array(
            [[rng.random() * (b - a) + a for [a, b] in self.bounds] for i in range(n)]
        )
        return pointArray

    def center(self):
        return np.array([(a + b) / 2 for [a, b] in self.bounds])


class UnitBoxWindow(BoxWindow):
    def __init__(self, center):
        """Create a Box window with bounds of length equal to 1

        Args:
            center (array): coordonnées du centre de la boîte.
        """

        bounds = np.array([[c - 0.5, c + 0.5] for c in center])

        super(BoxWindow, self).init(bounds)
