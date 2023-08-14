import unittest


def prod(x, y):
    if x == 7 and y == 9:
        return x * y
       # return "An insidious bu has surfaced!"
    else:
        return x * y


class ProductTestCase(unittest.TestCase):

    def test_integers(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                p = prod(x, y)
                self.assertEqual(p, x * y, "Integer multiplication failed")

    def test_floats(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                x = x / 10
                y = y / 10

                p = prod(x, y)
                self.assertEqual(p, x * y, "Float multiplication failed")

if __name__ == "__main__":
    unittest.main()