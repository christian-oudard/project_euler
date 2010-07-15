directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]

def adjacent_spots(blocks):
    """
    >>> sorted(list(adjacent_spots({(0, 1)})))
    [(-1, 1), (0, 2), (1, 1)]
    """
    blocks = set(blocks)
    adjacent = set()
    for block in blocks:
        x, y = block
        for dx, dy in directions:
            new_x = x + dx
            new_y = y + dy
            if new_y <= 0:
                continue
            new_spot = new_x, new_y
            if new_spot in blocks:
                continue
            adjacent.add(new_spot)
    return adjacent

def canonical(blocks):
    blocks = tuple(sorted(set(blocks)))
    flipped = tuple(sorted((-x, y) for x, y in blocks))
    if flipped < blocks:
        return flipped
    else:
        return blocks

def calc_x_center(blocks):
    return sum(x for x, y in blocks)

def next_generation(old_generation):
    for blocks in old_generation:
        for new_spot in adjacent_spots(blocks):
            x, y = new_spot
            new_blocks = blocks + (new_spot,)
            #new_blocks = canonical(new_blocks)
            yield new_blocks

# Use a tree structure to conserve memory
def trace(head_block):
    while head_block is not None:
        block, head_block = head_block
        yield block

def next_tree_generation(old_generation):
    for head_block in old_generation:
        blocks = list(trace(head_block))
        for new_spot in adjacent_spots(blocks):
            yield (new_spot, head_block)

def format_sculpture(blocks):
    blocks = list(blocks)
    blocks.append((0, 0))
    x_vals = []
    y_vals = []
    for x, y in blocks:
        x_vals.append(x)
        y_vals.append(y)
    min_x = min(x_vals)
    min_y = min(y_vals)
    max_x = max(x_vals)
    max_y = max(y_vals)
    blocks = [(x - min_x, y - min_y) for x, y in blocks]
    max_x -= min_x
    max_y -= min_y
    field = [[' '] * (max_x + 1) for _ in range(max_y + 1)]
    for x, y in blocks:
        field[max_y - y][x] = '#'
    return '\n'.join(''.join(row) for row in field)

gen = [((0, 1),)]

#
tree_gen = [
    ((0, 1), None),
]

#limit = 10
limit = 9
for i in range(1, limit + 1):
#    num_balanced = sum(1 for blocks in gen if calc_x_center(blocks) == 0)
#    print('gen {}: {} ({})'.format(str(i).rjust(2), num_balanced, len(gen)))
#    #for x_center, blocks in sorted(gen):
#    #    if x_center == 0:
#    #        print(format_sculpture(blocks))
#    #        print()

    #print('old  {}: {}'.format(i, len(gen)))
    print('tree {}: {}'.format(i, len(tree_gen)))

    if i >= limit:
        break

    #gen = set(next_generation(gen))
    tree_gen = set(next_tree_generation(tree_gen))
#
