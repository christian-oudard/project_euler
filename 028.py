# Number the rings from 0 to (num_rings - 1), r is used to denote the ring number.
# Each ring has size (2*r + 1), and marks out a square of area (2*r + 1)**2.
# The maximum entry in each ring is in the upper-right corner, and will be numbered (2*r + 1)**2.
# Going counter-clockwise along the ring, each corner entry will be 2*r less
# than the corner before it, since each side has length (2*r + 1).

# The sum of the four corners for each ring (excluding the first) is then:
# ((2*r + 1)**2) + ((2*r + 1)**2 - 2*r) + ((2*r + 1)**2 - 4*r) + ((2*r + 1)**2 - 6*r)
# == 4*(2*r + 1)**2 - 12*r

size = 1001 # The width of the outermost ring.
num_rings = (size + 1) // 2
print(1 + sum(4*(2*r + 1)**2 - 12*r for r in range(1, num_rings)))
