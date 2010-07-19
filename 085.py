from utility import memoize

def num_rectangles(width, height):
    """
    >>> num_rectangles(1, 1)
    1
    >>> num_rectangles(3, 1)
    6
    >>> num_rectangles(4, 1)
    10
    >>> num_rectangles(5, 1)
    15
    >>> num_rectangles(3, 2)
    18
    """
    if height == 0 or width == 0:
        return 0
    if width < height:
        width, height = height, width
    return _num_rectangles(width, height)

@memoize
def _num_rectangles(width, height):
    if height <= 1:
        return num_rectangles(width - 1, 1) + width
    return _num_rectangles(width, height - 1) + height * _num_rectangles(width, 1)

import itertools
def search(limit):
    answers = {}
    def answer(w, h, n):
        diff = abs(limit - n)
        answers[diff] = (w, h)

    for w in itertools.count(1):
        for h in itertools.count(1):
            n = num_rectangles(w, h)
            if n > limit:
                answer(w, h, n)
                answer(w, h-1, num_rectangles(w, h-1))
                if w == h:
                    min_diff = min(answers.keys())
                    w, h = answers[min_diff]
                    return w * h
                break

print(search(2000000))
