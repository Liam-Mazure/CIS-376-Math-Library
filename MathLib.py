
# Author: Cole Blunt, Liam
# Date: 2/13/2023
# Description: code contains math for vercors and a 4x4 matrix,
# a Vector3 class for 3d vectors
# a vector2 class for 2d vectors
# a Matrix class for 4x4 matrixs

import math

# Class to represent 3D vectors.
class Vector3():

    # Initialize a new Vector3 object with x, y, z, and w components.
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    # Calculate the cross product of this vector and another vector.
    def cross_product(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vector3(x, y, z, self.w)

    # Calculate the dot product of this vector and another vector.
    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    # Calculate the angle between this vector and another vector.
    def angle_between(self, other):
        dot_product = self.dot_product(other)
        magnitude_product = self.mag_with() * other.mag_with()
        if magnitude_product == 0:
            return 0

        angle = math.acos(min(1, max(-1, dot_product / magnitude_product)))
        return angle

    # Add this vector and another vector.
    def add_vec(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        w = self.w + other.w
        return Vector3(x, y, z, w)

    # Subtract another vector from this vector.
    def sub_vec(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Vector3(x, y, z, self.w)

    # Normalize this vector.
    def normalize(self):
        magnitude = self.mag_with()
        if magnitude == 0:
            return Vector3(0, 0, 0, self.w)
        return Vector3(self.x / magnitude, self.y / magnitude, self.z / magnitude, self.w)

    # Calculate the magnitude of this vector with the square root.
    def mag_with(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    # Calculate the magnitude of this vector without the square root.
    def mag_with_out(self):
        return self.x**2 + self.y**2 + self.z**2

    # Check if this vector is equal to another vector.
    def same_vec(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w

# This class represents a 2D vector
class Vector2:
    # The __init__ method sets the values of x, y, and w when creating a new Vector2 object.
    def __init__(self, x, y, w):
        self.x = x
        self.y = y
        self.w = w

    # This method computes the cross product of this vector and another vector.
    def cross_product(self, other):
        x = self.x * other.y
        y = self.y * other.x
        return Vector2(x, y, self.w)

    # This method computes the dot product of this vector and another vector.
    def dot_product(self, other):
        return self.x * other.x + self.y * other.y

    # This method calculates the angle between this vector and another vector.
    def angle_between(self, other):
        if self.x == 0 and self.y == 0:
            return 0
        if other.x == 0 and other.y == 0:
            return 0

        dot = self.dot_product(other)
        a_mag = self.mag_with()
        b_mag = other.mag_with()

        angle = math.acos(min(1, max(-1, dot / (a_mag * b_mag))))

        return angle

    # This method adds this vector and another vector and returns the result as a new Vector2 object.
    def add_vec(self, other):
        return Vector2(self.x + other.x, self.y + other.y, self.w)

    # This method subtracts another vector from this vector and returns the result as a new Vector2 object.
    def sub_vec(self, other):
        return Vector2(self.x - other.x, self.y - other.y, self.w)

    # This method returns a unit vector that points in the same direction as this vector.
    def normalize(self):
        magnitude = self.mag_with()
        if magnitude == 0:
            return Vector2(0, 0, self.w)
        return Vector2(self.x / magnitude, self.y / magnitude, self.w)

    # This method returns the magnitude (length) of this vector.
    def mag_with(self):
        return math.sqrt(self.x**2 + self.y**2)

    # This method returns the square of the magnitude of this vector, without taking the square root.
    def mag_with_out(self):
        return self.x**2 + self.y**2

    # Check if this vector is equal to another vector.
    def same_vec(self, other):
        return self.x == other.x and self.y == other.y and self.w == other.w

class Matrix():

    # Initialize the matrix with data and set rows and cols attributes
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    # Return the shape of the matrix as a tuple of (rows, columns)
    def shape(self):
        return(self.rows, self.cols)

    # Add two matrices
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

    # Subtract two matrices
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

    # Multiply a matrix by a vector
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

    # Multiply two matrices
    def mult_by_mtx(self, other):
        if self.cols != other.rows:
            raise ValueError("The number of columns in the first matrix must be the same as the number of rows in the second matrix")

        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                sum = 0
                for k in range(other.rows):
                    sum += self.data[i][k] * other.data[k][j]
                row.append(sum)
            result.append(row)

        return result

    # returns true if same matrix
    def same_mtx(self, other):
        if self.shape() != other.shape():
            return False

        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j]  != other.data[i][j]:
                    return False
        return True