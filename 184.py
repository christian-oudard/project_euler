import time
from utility import all_pairs

#TODO speed optimization
# don't duplicate triangles, track visited segments
# use symmetry, canonical positioning
# profiling optimization
# optimize multiplications

known_solutions = {
    2: 8,
    3: 360,
    4: 2768,
    5: 10600,
    6: 45976,
    7: 111368,
    8: 270720,
    9: 591152,
    10: 1101232,
    11: 2039688,
}

def main():
    start_all = time.time()
    for r in range(2, 7):
        print('---')
        print('r =', r)
        start = time.time()
        t = find_triangles(r)
        print(t)
        assert(known_solutions[r] == t)
        end = time.time()
        print('%.3fs' % (end - start))
    end_all = time.time()
    print('===')
    print('total')
    print('%.3fs' % (end_all - start_all))

def find_triangles(radius):
    radius2 = radius ** 2
    # generate points in circle, except origin
    r = range(-radius + 1, radius)
    points = set()
    for x in r:
        for y in r:
            if mag2(x, y) < radius2:
                points.add((x, y))
    points.remove((0,0))

    #print(points)
    triangles = set()
    for p1, p2 in all_pairs(points):
        # test if p1-p2 crosses the origin
        if cmp_line(p1, p2, (0,0)) == 0:
            continue
        # get the set of points p3 that is on the side of the line p1-(0,0)
        # farthest from p2, and likewise for p2-(0,0). each of these points
        # completes a triangle (p1, p2, p3) that contains the origin.
        #TODO prevent duplication of triangles, reducing reliance on sets
        p3_set = (partition(points, p1, (0,0), p2, reverse=True) &
                  partition(points, p2, (0,0), p1, reverse=True))
        for p3 in p3_set:
            triangles.add(frozenset((p1, p2, p3)))
    return len(triangles)

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

def partition(points, l1, l2, s, reverse=False):
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
    if reverse:
        sign = -sign
    if sign == 0:
        raise ValueError('s is on the line l1 l2')
    return set(p for p in points if cmp_line(l1, l2, p) == sign)

def mag2(x, y):
    return x**2 + y**2

main()
#import doctest
#doctest.testmod()
