
def is_triangle(f):
    def inner(sides):
        a, b, c = sorted(sides)
        return a * b * c != 0 and a + b >= c and f(sides)
    return inner

@is_triangle
def equilateral(sides):
    return len(set(sides)) == 1

@is_triangle
def isosceles(sides):
    return len(set(sides)) < 3

@is_triangle
def scalene(sides):
    return len(set(sides)) == 3

