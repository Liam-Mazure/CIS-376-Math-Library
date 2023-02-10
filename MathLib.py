import math

class Vector3():
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def cross_product(self, other):
            x = self.y * other.z - self.z * other.y
            y = self.z * other.x - self.x * other.z
            z = self.x * other.y - self.y * other.x
            return Vector3(x, y, z, self.w)

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
        return Vector3(x, y, z, w)

    def sub_vec(self, other):
            x = self.x - other.x
            y = self.y - other.y
            z = self.z - other.z
            return Vector3(x, y, z, self.w)
    
    def normalize(self):
        magnitude = self.mag_with()
        if magnitude == 0:
            return Vector3(0, 0, 0, self.w)
        return Vector3(self.x / magnitude, self.y / magnitude, self.z / magnitude, self.w)

    def mag_with(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def mag_with_out(self):
        return self.x**2 + self.y**2 + self.z**2

    def same_vec(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w

class Vector2():
    def __init__(self, x, y, w):
        self.x = x
        self.y = y
        self.w = w

    def cross_product(self, other):
        x = self.x * other.y
        y = self.y * other.x
        return Vector2(x, y,self.w)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y

    def angle_between(self, other):
        dot = self.dot_product(other)
        a_mag = self.mag_with()
        b_mag = self.mag_with_out()

        angle = math.acos(min(1, max(dot / a_mag * b_mag)))
    
        return angle

    def add_vec(self, other):
        return Vector2(self.x + other.x, self.y + other.y, self.w)

    def sub_vec(self, other):
        return Vector2(self.x - other.x, self.y - other.y, self.w)
    
    def normalize(self):
        magnitude = self.mag_with()
        if magnitude == 0:
            return Vector2(0, 0, self.w)
        return Vector2(self.x / magnitude, self.y / magnitude, self.w)
        
    def mag_with(self):
        return math.sqrt(self.x**2 + self.y**2)
        
    def mag_with_out(self):
        return self.x**2 + self.y**2

    def same_vec(self, other):
        return self.x == other.x and self.y == other.y and self.w == other.w

class Matrix():
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def shape(self):
        return(self.rows, self.cols)
    
    def add_mtx(self, other):
        if self.shape() != other.shape():
            raise ValueError("Matrcies must be the same size")
        
        result = []

        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] + other.data[i][j])
                result.append(row)
        
        return result

    def sub_mtx(self, other):
        if self.shape() != other.shape():
            raise ValueError("Matrcies must be the same size")
        
        result = []

        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] - other.data[i][j])
                result.append(row)
        
        return result

    def mult_by_vec(self, vec):
        if self.cols != len(vec):
            raise ValueError("Must have the same number of columns in matrix as elements in the vector")
        
        result = []

        for i in range(self.rows):
            sum = 0
            for j in range(self.cols):
                sum += self.data[i][j] * vec[j]
            result.append(sum)

        return result

    def mult_by_mtx(self,other):
        if self.shape() != other.shape():
            raise ValueError("Matrcies must be the same size")
        
        result = []

        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                total = 0
                for k in range(self.cols):
                    sum += self.data[i][k] * other.data[k][j]
                row.append(sum)
            result.append(row)
        
        return result

    def same_mtx(self, other):
        if self.shape() != other.shape():
            return False

        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j]  != other.data[i][j]:
                    return False
        
        return True