import unittest
import random
from math_quiz import generate_random_integer, generate_random_operator, generate_equation_and_solution

class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        """Test if random numbers generated are within given range."""
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        """Test if generated operator is one of the allowed ones."""
        operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random values
            rand_operator = generate_random_operator()
            self.assertIn(rand_operator, operators)

    def test_generate_equation_and_solution(self):
        """Test the equation generation and correct answer calculation."""
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (6, 3, '-', '6 - 3', 3),
            (4, 5, '*', '4 * 5', 20),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            equation, answer = generate_equation_and_solution(num1, num2, operator)
            self.assertEqual(equation, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
