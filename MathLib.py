import math

class Vector2():
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def cross_product(self, other):
            x = self.y * other.z - self.z * other.y
            y = self.z * other.x - self.x * other.z
            z = self.x * other.y - self.y * other.x
            return Vector2(x, y, z, self.w)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def angle_between(self, other):
        dot_product = self.dot_product(other)
        magnitude_product = self.mag_with() * other.mag_with()

        if magnitude_product == 0:
            return 0

        angle = math.acos(min(1, max(-1, dot_product / magnitude_product)))
        return angle

    def add_vec(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        w = self.w + other.w
        return Vector2(x, y, z, w)

    def sub_vec(self, other):
            x = self.x - other.x
            y = self.y - other.y
            z = self.z - other.z
            return Vector2(x, y, z, self.w)
    
    def normalize(self):
        magnitude = self.mag_with()
        if magnitude == 0:
            return Vector2(0, 0, 0, self.w)
        return Vector2(self.x / magnitude, self.y / magnitude, self.z / magnitude, self.w)

    def mag_with(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2 + self.w**2)

    def mag_with_out(self):
        return self.x**2 + self.y**2 + self.z**2 + self.w**2

    def same_vec(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w

class Vector3():
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def cross_product(self):
        pass

    def dot_product(self):
        pass

    def angle_between(self):
        pass

    def add_vec(self):
        pass

    def sub_vec(self):
        pass
    
    def normalize(self):
        pass

    def mag_with(self):
        pass

    def mag_with_out(self):
        pass

    def same_vec(self):
        pass

class Matrix():
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def add_mtx(self):
        pass

    def sub_mtx(self):
        pass

    def mult_by_vec(self):
        pass

    def mult_by_mtx(self):
        pass

    def same_mtx(self):
        pass