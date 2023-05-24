import math

x = .4
y = .2
z = 1

xr1 = 1
yr1 = 2
zr1 = 3

xr2 = 1
yr2 = 2
zr2 = 3

"""
Linear vectors take in the x, y, and z components of a vector and return dict as a vector object.
The dict contains a magnatude in meters/second^2, theta (xy axis), and gamma (yz) axis components
"""
class LinearVector:
    def __init__(self, x, y, z):
        # calculate the hypotenuce of the XY plane
        c = math.sqrt((x ** 2) + (y ** 2))
        # Then use it as the base of a triangle on the XZ plane
        hypotenuce = math.sqrt((c ** 2) + (z ** 2))
        self.magnitude = math.sqrt((hypotenuce ** 2) + (z ** 2))

        # Calculate direction of vector on xy plane
        # Quadrant 1
        if x > 0 and y > 0:
            self.θ = math.degrees(math.atan(abs(y/x)))
        # Quadrant 2
        elif x < 0 and y > 0:
            self.θ = 180 - math.degrees(math.atan(abs(y/x)))
        # Quadrant 3
        elif x < 0 and y < 0:
            self.θ = 180 + math.degrees(math.atan(abs(y/x)))
        # Quadrant 4
        elif x > 0 and y < 0:
            self.θ = 360 - math.degrees(math.atan(abs(y/x)))
        
        # Calculate direction of vector on yz plane
        # Quadrant 1
        if hypotenuce > 0 and z > 0:
            self.γ = math.degrees(math.atan(abs(z/hypotenuce)))
        # Quadrant 2
        elif hypotenuce < 0 and z > 0:
            self.γ = 180 - math.degrees(math.atan(abs(z/hypotenuce)))
        # Quadrant 3
        elif hypotenuce < 0 and z < 0:
            self.γ = 180 + math.degrees(math.atan(abs(z/hypotenuce)))
        # Quadrant 4
        elif hypotenuce > 0 and z < 0:
            self.γ = 360 - math.degrees(math.atan(abs(z/hypotenuce)))

    def r(self):
        return {"magnitude":self.magnitude,
                "theta": self.θ,
                "gamma": self.γ}

"""Receives degree and retuns degrees/second"""
"""
class RotationalVector:
    def __init__(self, xr1, yr1, zr1,):
        self.xr = xr
        self.yr = yr
        self.zr = zr

    def r(self):
        return {"x-rotation": xr,
                "y-rotation": yr,
                "z-rotation": zr}
"""

v1 = LinearVector(x, y, z)
print(v1.r())
