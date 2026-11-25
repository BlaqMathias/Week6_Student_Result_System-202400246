
import unittest

from grading import calculate_grade


class TestGrading(unittest.TestCase):

    def test_grade_a_boundary(self):
        self.assertEqual(calculate_grade(70), "A")

    def test_grade_b_boundary(self):
        self.assertEqual(calculate_grade(60), "B")

    def test_grade_f(self):
        self.assertEqual(calculate_grade(0), "F")

    def test_invalid_high_score(self):
        with self.assertRaises(ValueError):
            calculate_grade(101)


if __name__ == "__main__":
    unittest.main()
