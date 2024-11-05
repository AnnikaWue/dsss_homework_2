import random


def generate_random_integer(min, max):
    """
    Generate a random integer between min_value and max_value.
    
    Args:
        min (int): Minimum integer value.
        max (int): Maximum integer value.

    Returns:
        int: A random integer within the given range.
    """
    return random.randint(min, max)


def generate_random_operator():
    """
    Randomly select one of the given mathematical operator.
    
    Returns:
        str: A randomly selected operator ('+', '-', or '*').
    """
    return random.choice(['+', '-', '*'])


def generate_equation_and_solution(num1, num2, operator):
    """
    Create an equation and calculate the correct answer.

    Args:
        num1 (int): The first operand.
        num2 (int): The second operand.
        operator (str): The mathematical operator ('+', '-', or '*').

    Returns:
        tuple: A tuple containing the problem string and the correct answer.
    """
    equation = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    else:
        raise ValueError("Unsupported operator. Only '+', '-', and '*' are allowed.")
    
    return equation, answer

def math_quiz():
    """
    Main function to run the math quiz. A player gets randomly generated equations and inputs an answer. If the answer is correct, the player gets a point.
    """
    score = 0
    total_questions = 3  # Number of questions in the quiz


    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate two random numbers and an operator for the problem
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 6)
        operator = generate_random_operator()

        # Generate the equation and the correct answer
        equation, correct_answer = generate_equation_and_solution(num1, num2, operator)
        print(f"\nQuestion: {equation}")

        # Get user input and add error handling
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Only integers allowed!")
            continue

        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    # Display the final score
    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
