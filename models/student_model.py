from pydantic import BaseModel


class StudentBase(BaseModel):
    """Common student fields."""
    name: str
    email: str
    course: str
    semester: int


class StudentCreate(StudentBase):
    """Request schema for creating a new student."""
    pass


class StudentUpdate(BaseModel):
    """Request schema for updating an existing student."""
    name: str | None = None
    email: str | None = None
    course: str | None = None
    semester: int | None = None


class Student(StudentBase):
    """Response schema representing a stored student record with unique ID."""
    id: int
