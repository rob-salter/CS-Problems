def is_triangle(sides):
    if sum(sorted(sides)[0:2]) > sorted(sides)[2] and sum(sides) != 0:
        return True   

def equilateral(sides):   
    return is_triangle(sides) and len(set(sides)) == 1


def isosceles(sides):
   
    return is_triangle(sides) and len(set(sides)) <= 2 


def scalene(sides):

    return is_triangle(sides) and len(set(sides)) == 3 