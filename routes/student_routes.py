"""FastAPI Routes for Student CRUD operations."""
from fastapi import APIRouter, Query, Response, status
from fastapi.responses import JSONResponse

from controllers import student_controller
router = APIRouter(
    prefix="/students",
    tags=["Students"],
)


@router.post(
    "",
    response_model=dict,
    status_code=status.HTTP_201_CREATED,
    summary="Create Student",
    description="Create a new student record. Returns 201 Created on success.",
)
def create_student_endpoint(student: dict) -> dict:
    """Create a new student record."""
    return student_controller.create_student(student)


@router.get(
    "",
    response_model=list[dict],
    status_code=status.HTTP_200_OK,
    summary="Read All Students",
    description="Retrieve a list of all students with optional filtering and pagination.",
)
def get_all_students_endpoint(
    name: str | None = Query(default=None, description="Filter students by name (case-insensitive substring)"),
    course: str | None = Query(default=None, description="Filter students by course (case-insensitive substring)"),
    semester: int | None = Query(default=None, ge=1, le=12, description="Filter students by semester"),
    skip: int = Query(default=0, ge=0, description="Number of records to skip (pagination)"),
    limit: int = Query(default=100, ge=1, le=100, description="Max number of records to return"),
) -> list[dict]:
    """Retrieve all student records."""
    return student_controller.get_all_students(
        name=name,
        course=course,
        semester=semester,
        skip=skip,
        limit=limit,
    )


@router.get(
    "/{id}",
    response_model=dict,
    status_code=status.HTTP_200_OK,
    summary="Read Student by ID",
    description="Retrieve a single student record by their unique ID. Returns 404 if not found.",
)
def get_student_by_id_endpoint(id: int) -> dict | JSONResponse:
    """Retrieve a student record by ID."""
    student = student_controller.get_student_by_id(student_id=id)
    if student is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": f"Student with ID {id} not found"},
        )
    return student


@router.put(
    "/{id}",
    response_model=dict,
    status_code=status.HTTP_200_OK,
    summary="Update Student",
    description="Update an existing student record by ID. Returns 404 if not found.",
)
def update_student_endpoint(id: int, student_data: dict) -> dict | JSONResponse:
    """Update a student record by ID."""
    updated_student = student_controller.update_student(
        student_id=id,
        student_data=student_data,
    )
    if updated_student is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": f"Student with ID {id} not found"},
        )
    return updated_student


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete Student",
    description="Delete a student record by ID. Returns 204 No Content with empty body on success, or 404 if not found.",
)
def delete_student_endpoint(id: int) -> Response:
    """Delete a student record by ID."""
    deleted = student_controller.delete_student(student_id=id)
    if not deleted:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": f"Student with ID {id} not found"},
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)
