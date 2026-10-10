"""Custom exceptions and validation helpers."""

class StudentNotFoundError(Exception):
    """Raised when a queried student ID does not exist."""
    pass

class DuplicateStudentError(Exception):
    """Raised when attempting to add a student ID that already exists."""
    pass

def validate_gpa(val: str) -> float:
    """Validate that input can be cast to a float between 0.0 and 10.0."""
    try:
        gpa = float(val)
        if not (0.0 <= gpa <= 10.0):
            raise ValueError
        return round(gpa,2)
    except (ValueError, TypeError):
        raise ValueError("GPA must be a valid number between 0.0 and 10.0.")