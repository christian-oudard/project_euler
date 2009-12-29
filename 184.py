import time
from utility import all_pairs, cmp_line, partition

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
        p3_set = (partition(points, p1, (0,0), p2)[1] &
                  partition(points, p2, (0,0), p1)[1])
        for p3 in p3_set:
            triangles.add(frozenset((p1, p2, p3)))
    return len(triangles)

def mag2(x, y):
    return x**2 + y**2

if __name__ == '__main__':
    main()
