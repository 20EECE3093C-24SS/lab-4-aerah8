# TODO-1: add convert_to_letter_grade(score) function
    
def convert_to_letter_grade(score):
    """
    Converts a numerical score into a corresponding letter grade.

    Args:
        score (int, float): The numerical score to convert into a letter grade.

    Returns:
        str: The upper-case letter grade corresponding to the numerical score.

    Raises:
        ValueError: If the score is outside the range of 0 to 100.
        TypeError: If the score is not a numeric value (int or float).

    """
    # Check if the score is an integer or float
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a numeric value.")

    # Check if the score is within the valid range
    if not (0 <= score <= 100):
        raise ValueError("Score must be between 0 and 100.")

    # Determine the letter grade based on the score range
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    else:
        return "F"

# Example usage:
# print(convert_to_letter_grade(85))  # Output: B
