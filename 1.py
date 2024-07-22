import math

def get_circle_area(radius):
    if radius <= 0:
        raise ValueError("Radius must be positive.")
    return math.pi * radius * radius

def get_triangle_area(side1, side2, side3):
    if any(side <= 0 for side in [side1, side2, side3]):
        raise ValueError("Sides of a triangle must be positive.")
    sp = (side1 + side2 + side3) / 2
    area = math.sqrt(sp * (sp - side1) * (sp - side2) * (sp - side3))
    return area
