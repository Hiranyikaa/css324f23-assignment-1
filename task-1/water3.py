def initial_state():
    return (8, 0, 0)

def is_goal(s):

    return s[0] == 4 and s[1] == 4

def successors(s):
    a, b, c = s
    t = 8 - a
    if (b > 0 or c > 0) and t > 0:
        if b > t:
            yield((8, b-t, c), t)
        if c > t:
            yield((8, b, c-t), t)
        if b < t:
            yield((a+b, 0, c), b)
        if c < t:
            yield ((a+c, b, 0), c)
    t = 5 - b
    if (a > 0 or c >0) and t > 0:
        if a > t:
            yield ((a-t, 5, c), t)
        if c > t:
            yield ((a, 5, c-t), t)
        if a < t:
            yield ((0, b+a, c), a)
        else:
            yield ((a, b+c, 0), c)
    t = 3 - c
    if (a > 0 or b > 0) and t > 0:
        if a > t:
            yield((a-t, b, 3), t)
        if b > t:
            yield((a, b-t, 3), t)
        if a < t:
            yield((0, b, c+a), a)
        else:
            yield((a, 0, c+b), b)
