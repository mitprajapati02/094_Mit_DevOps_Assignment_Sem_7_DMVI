def build_student(data: dict, student_id: int | None = None) -> dict:
    """Build a plain student dictionary for storage or an API response."""
    student = dict(data)
    if student_id is not None:
        student["id"] = student_id
    return student
