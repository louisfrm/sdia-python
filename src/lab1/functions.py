def is_unique(x):
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> d9f6fe079c2404c909d51649e845091445af26c3
    if x == []:
        return True
    else:
        y = x.pop()
        if y in x:
            return False
        else:
            return is_unique(x)


def triangle_shape(height):
    triangle = str()
    for i in range(height):
        for j in range(height - i - 1):
            triangle += " "
        for j in range(2 * i + 1):
            triangle += "x"
        for j in range(height - i - 1):
            triangle += " "
        if i != height - 1:
            triangle += "\n"
    return triangle
<<<<<<< HEAD


def is_unique_corr(x):

=======
=======
>>>>>>> d9f6fe079c2404c909d51649e845091445af26c3
    """Check that ``x`` has no duplicate elements.

    Args:
        x (list): elements to be compared.

    Returns:
        bool: True if ``x`` has duplicate elements, otherwise False
    """
    return len(set(x)) == len(x)


<<<<<<< HEAD
def triangle_shape_corr(n, fillchar="x", spacechar=" "):
=======
def triangle_shape(n, fillchar="x", spacechar=" "):
>>>>>>> d9f6fe079c2404c909d51649e845091445af26c3
    """Return a string made of ``fillchar`` and ``spacechar``representing a triangle shape of height ``n``.

    For n=0, return ``""``.

    .. testcode::

        from lab1.functions import triangle_shape
        print(triangle_shape(6, fillchar="x", spacechar="_"))

    .. testoutput::

        _____x_____
        ____xxx____
        ___xxxxx___
        __xxxxxxx__
        _xxxxxxxxx_
        xxxxxxxxxxx

    Args:
        n (int): height of the triangle.
        fillchar (str, optional): Defaults to "x".
        spacechar (str, optional): Defaults to " ".

    Returns:
        str: string representation of the triangle.
    """
    width = 2 * n - 1
    return "\n".join(
        (fillchar * (2 * i + 1)).center(width, spacechar) for i in range(n)
    )
<<<<<<< HEAD
=======
>>>>>>> 8b6e677be189599065f3c5076500fcfe1e3d736e
>>>>>>> d9f6fe079c2404c909d51649e845091445af26c3
