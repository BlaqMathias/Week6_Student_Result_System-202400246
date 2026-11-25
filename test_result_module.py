
import unittest

from result_module import calculate_gpa, calculate_total_score, generate_result


class TestResultModule(unittest.TestCase):

    def test_calculate_total_score(self):
        total = calculate_total_score(18, 17, 52)
        self.assertEqual(total, 87)

    def test_generate_result(self):
        result = generate_result(
            "John",
            "CSC/2026/001",
            "SWE 306",
            18,
            17,
            52
        )

        self.assertEqual(result["total"], 87)
        self.assertEqual(result["grade"], "A")
        self.assertEqual(result["grade_point"], 5)

    def test_calculate_gpa(self):
        courses = [
            {"grade_point": 5, "credit_unit": 3},
            {"grade_point": 4, "credit_unit": 2},
            {"grade_point": 3, "credit_unit": 3}
        ]

        self.assertEqual(calculate_gpa(courses), 4.0)

    def test_invalid_assignment_score(self):
        with self.assertRaises(ValueError):
            calculate_total_score(25, 17, 52)

    def test_empty_course_results(self):
        with self.assertRaises(ValueError):
            calculate_gpa([])


if __name__ == "__main__":
    unittest.main()
