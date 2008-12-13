from utility import all_pairs

radius = 2
radius2 = radius ** 2

def main():
    # generate points in circle, except origin
    #TODO precompute x2 and y2 for whole range
    r = range(-radius + 1, radius)
    points = set()
    for x in r:
        for y in r:
            if mag2(x, y) < radius2:
                points.add((x, y))
    points.remove((0,0))

    #print(points)
    for p1, p2 in all_pairs(points):
        if line_crosses_origin(p1, p2):
            continue
        #stub

    # when a triangle is found, remove its segments from the set
    # no, triangles can duplicate one line segment
    # find a canonical version of the triangle... designate triangles with a primary segment and far point

def cmp_line(l1, l2, p):
    """
    Determine where the point p lies with relation to the line l1-l2.
    Return -1 if s is below, +1 if it is above, and 0 if it is on the line.

    >>> cmp_line((-1,-1), (1,1), (1,0))
    -1
    >>> cmp_line((-1,-1), (1,1), (0,1))
    1
    >>> cmp_line((-1,-1), (1,1), (0,0))
    0

    It also works with vertical lines.
    >>> cmp_line((0,-1), (0,1), (1, 0))
    -1
    >>> cmp_line((0,-1), (0,1), (-1, 0))
    1
    >>> cmp_line((0,-1), (0,1), (0, 0))
    0
    """
    x1, y1 = l1
    x2, y2 = l2
    x, y = p
    dy = y2 - y1
    dx = x2 - x1
    return cmp(y * dx, dy * (x - x1) + y1 * dx)

def partition(points, l1, l2, s):
    """
    Partition a set of points by a line.

    The line is defined by l1, l2. The desired side of the line is given by the point s.

    >>> partition([(-1,0), (0,0), (1,0)], (0,1), (0,-1), (2,0))
    {(1, 0)}
    >>> partition([(-1,0), (0,0), (1,0)], (0,1), (0,-1), (-2,0))
    {(-1, 0)}
    >>> partition([(-2,2), (-1,0), (0,0), (1,0)], (-1,0), (0,1), (3,0)) == {(0, 0), (1, 0)}
    True
    >>> partition([(-2,2), (-1,0), (0,0), (1,0)], (-1,0), (0,1), (-3,0)) == {(-2, 2)}
    True
    """
    if l1 == l2:
        raise ValueError('l1 equals l2')
    sign = cmp_line(l1, l2, s)
    if sign == 0:
        raise ValueError('s is on the line l1 l2')
    return set(p for p in points if cmp_line(l1, l2, p) == sign)

def line_crosses_origin(l1, l2):
    """
    See whether a line segment with integral endpoints contains the origin.

    >>> line_crosses_origin((0,0), (0,0))
    True
    >>> line_crosses_origin((-1,0), (1,0))
    True
    >>> line_crosses_origin((0,-1), (0,1))
    True
    >>> line_crosses_origin((-1,-1), (1,1))
    True
    >>> line_crosses_origin((1,1), (2,2))
    False
    >>> line_crosses_origin((0,1), (1,2))
    False
    """
    x1, y1 = l1
    x2, y2 = l2
    # test that line segment intersects both axes
    if (not in_range(0, x1, x2) or
        not in_range(0, y1, y2)):
        return False
    # test that line, if infinite, would pass through origin
    return cmp_line(l1, l2, (0,0)) == 0

def in_range(n, lo, hi):
    """
    Test that a number n is in the range [lo, hi] inclusive.

    >>> in_range(0, 0, 0)
    True
    >>> in_range(-1, 0, 1)
    False
    >>> in_range(0, -1, 1)
    True
    >>> in_range(0, 1, -1)
    True
    """
    if lo > hi:
        (lo, hi) = (hi, lo)
    return lo <= n <= hi

def mag2(x, y):
    return x**2 + y**2

#main()
import doctest
doctest.testmod()
