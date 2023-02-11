import unittest
import math

from MathLib import Vector3
from MathLib import Vector2
from MathLib import Matrix


class TestVector3(unittest.TestCase):
    def test_cross_product(self):
        v1 = Vector3(1, 2, 3, 0)
        v2 = Vector3(4, 5, 6, 0)
        result = v1.cross_product(v2)

        self.assertAlmostEqual(-3, result.x)
        self.assertAlmostEqual(6, result.y)
        self.assertAlmostEqual(-3, result.z)

    def test_cross_product_zero_vector(self):
        v1 = Vector3(0, 0, 0, 0)
        v2 = Vector3(1, 2, 3, 0)
        result = v1.cross_product(v2)

        self.assertAlmostEqual(0, result.x)
        self.assertAlmostEqual(0, result.y)
        self.assertAlmostEqual(0, result.z)

    def test_dot_product(self):
        v1 = Vector3(1, 2, 3, 1)
        v2 = Vector3(4, 5, 6, 1)
        result = v1.dot_product(v2)

        self.assertAlmostEqual(32, result)

    def test_dot_product_orthogonal_vectors(self):
        v1 = Vector3(1, 0, 0, 1)
        v2 = Vector3(0, 1, 0, 1)
        result = v1.dot_product(v2)

        self.assertAlmostEqual(0, result)

    def test_angle_between(self):
        v1 = Vector3(1, 2, 3, 0)
        v2 = Vector3(4, 5, 6, 0)
        result = v1.angle_between(v2)

        dot_product = v1.dot_product(v2)
        magnitude_product = v1.mag_with() * v2.mag_with()
        expected = math.acos(min(1, max(-1, dot_product / magnitude_product)))

        self.assertAlmostEqual(expected, result)

    def test_angle_between_zero_vectors(self):
        v1 = Vector3(0, 0, 0, 0)
        v2 = Vector3(0, 0, 0, 0)
        result = v1.angle_between(v2)

        self.assertAlmostEqual(0, result)

    def test_angle_between_parallel_vectors(self):
        v1 = Vector3(1, 2, 3,0)
        v2 = Vector3(2, 4, 6,0)
        result = v1.angle_between(v2)

        self.assertAlmostEqual(0, result)

    def test_angle_between_orthogonal_vectors(self):
        v1 = Vector3(1, 0, 0, 0)
        v2 = Vector3(0, 1, 0, 0)
        result = v1.angle_between(v2)

        self.assertAlmostEqual(math.pi / 2, result)

    def test_add_vec(self):
        v1 = Vector3(1, 2, 3, 0)
        v2 = Vector3(4, 5, 6, 0)
        result = v1.add_vec(v2)

        self.assertEqual(5, result.x)
        self.assertEqual(7, result.y)
        self.assertEqual(9, result.z)
        self.assertEqual(0, result.w)

    def test_sub_vec(self):
        v1 = Vector3(1, 2, 3, 0)
        v2 = Vector3(4, 5, 6, 0)
        result = v1.sub_vec(v2)

        self.assertEqual(-3, result.x)
        self.assertEqual(-3, result.y)
        self.assertEqual(-3, result.z)
        self.assertEqual(0, result.w)

    def test_normalize(self):
        v = Vector3(3, 4, 5, 0)
        result = v.normalize()
        self.assertAlmostEqual(1, result.mag_with())
        self.assertAlmostEqual(3 / v.mag_with(), result.x)
        self.assertAlmostEqual(4 / v.mag_with(), result.y)
        self.assertAlmostEqual(5 / v.mag_with(), result.z)

    def test_magnitude(self):
        v = Vector3(1,2,3,0)
        result = v.mag_with_out()
        self.assertAlmostEqual(14, result)

    def test_same_vec(self):
        v1 = Vector3(1, 2, 3, 0)
        v2 = Vector3(1, 2, 3, 0)
        v3 = Vector3(4, 5, 6, 0)
        self.assertTrue(v1.same_vec(v2))
        self.assertFalse(v1.same_vec(v3))

#Vestor2 Tests
class TestVector2(unittest.TestCase):
    def test_cross_product(self):
        v1 = Vector2(1, 2, 0)
        v2 = Vector2(4, 5, 0)
        result = v1.cross_product(v2)

        self.assertAlmostEqual(5, result.x)
        self.assertAlmostEqual(8, result.y)

    def test_cross_product_zero_vector(self):
        v1 = Vector2(0, 0, 0)
        v2 = Vector2(1, 2, 0)
        result = v1.cross_product(v2)

        self.assertAlmostEqual(0, result.x)
        self.assertAlmostEqual(0, result.y)

    def test_dot_product(self):
        v1 = Vector2(1, 2, 1)
        v2 = Vector2(3, 4, 1)
        result = v1.dot_product(v2)

        self.assertAlmostEqual(11, result)

    def test_dot_product_orthogonal_vectors(self):
        v1 = Vector2(1, 0, 1)
        v2 = Vector2(0, 1, 1)
        result = v1.dot_product(v2)

        self.assertAlmostEqual(0, result)

    def test_angle_between(self):
        v1 = Vector2(1, 2, 0)
        v2 = Vector2(3, 4, 0)
        result = v1.angle_between(v2)

        dot_product = v1.dot_product(v2)
        magnitude_product = v1.mag_with() * v2.mag_with()
        expected = math.acos(min(1, max(-1, dot_product / magnitude_product)))

        self.assertAlmostEqual(expected, result)

    def test_angle_between_zero_vectors(self):
        v1 = Vector2(0, 0, 0)
        v2 = Vector2(0, 0, 0)
        result = v1.angle_between(v2)

        self.assertAlmostEqual(0, result)

    def test_angle_between_parallel_vectors(self):
        v1 = Vector2(1, 2, 0)
        v2 = Vector2(2, 4, 0)
        result = v1.angle_between(v2)

        self.assertAlmostEqual(0, result)

    def test_angle_between_orthogonal_vectors(self):
        v1 = Vector2(1, 0, 0)
        v2 = Vector2(0, 1, 0)
        result = v1.angle_between(v2)

        self.assertAlmostEqual(math.pi / 2, result)

    def test_add_vec(self):
        v1 = Vector2(1, 2, 0)
        v2 = Vector2(4, 5, 0)
        result = v1.add_vec(v2)

        self.assertEqual(5, result.x)
        self.assertEqual(7, result.y)
        self.assertEqual(0, result.w)

    def test_sub_vec(self):
        v1 = Vector2(1, 2, 0)
        v2 = Vector2(4, 5, 0)
        result = v1.sub_vec(v2)

        self.assertEqual(-3, result.x)
        self.assertEqual(-3, result.y)
        self.assertEqual(0, result.w)

    def test_normalize(self):
        v = Vector2(3, 4, 0)
        result = v.normalize()
        self.assertAlmostEqual(1, result.mag_with())
        self.assertAlmostEqual(3 / v.mag_with(), result.x)
        self.assertAlmostEqual(4 / v.mag_with(), result.y)

    def test_magnitude(self):
        v = Vector2(1,2,0)
        result = v.mag_with_out()
        self.assertAlmostEqual(5, result)

    def test_same_vec(self):
        v1 = Vector2(1, 2, 0)
        v2 = Vector2(1, 2, 0)
        v3 = Vector2(4, 5, 0)
        self.assertTrue(v1.same_vec(v2))
        self.assertFalse(v1.same_vec(v3))

class TestMatrix(unittest.TestCase):
    def test_init(self):
        data = [[1, 2, 3], [4, 5, 6]]
        mtx = Matrix(data)
        self.assertEqual((2, 3), mtx.shape())
        self.assertEqual(data, mtx.data)

    def test_add_mtx(self):
        mtx1 = Matrix([[1, 2, 3], [4, 5, 6]])
        mtx2 = Matrix([[6, 5, 4], [3, 2, 1]])
        result = mtx1.add_mtx(mtx2)
        expected = [[7, 7, 7], [7, 7, 7]]
        self.assertEqual(expected, result)

    def test_sub_mtx(self):
        mtx1 = Matrix([[1, 2, 3], [4, 5, 6]])
        mtx2 = Matrix([[6, 5, 4], [3, 2, 1]])
        result = mtx1.sub_mtx(mtx2)
        expected = [[-5, -3, -1], [1, 3, 5]]
        self.assertEqual(expected, result)

    def test_mult_by_vec(self):
        mtx = Matrix([[1, 2, 3], [4, 5, 6]])
        vec = [1, 2, 3]
        result = mtx.mult_by_vec(vec)
        expected = [14, 32]
        self.assertEqual(expected, result)

    def test_mult_by_mtx(self):
        mtx1 = Matrix([[1, 2, 3], [4, 5, 6]])
        mtx2 = Matrix([[6, 5], [4, 3], [2, 1]])
        result = mtx1.mult_by_mtx(mtx2)
        expected = [[20, 14], [56, 41]]
        self.assertEqual(expected, result)

    def test_same_mtx(self):
        mtx1 = Matrix([[1, 2, 3], [4, 5, 6]])
        mtx2 = Matrix([[1, 2, 3], [4, 5, 6]])
        mtx3 = Matrix([[1, 2, 3], [4, 5, 7]])
        self.assertTrue(mtx1.same_mtx(mtx2))
        self.assertFalse(mtx1.same_mtx(mtx3))


if __name__ == '__main__':
    unittest.main()