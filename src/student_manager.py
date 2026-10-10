import csv
import json
import os
from typing import Dict, List, Optional
from src.utils import StudentNotFoundError, DuplicateStudentError

class StudentManager:
    def __init__(self, json_path: str = "data/students.json", csv_path: str = "data/students.csv"):
        self.json_path = json_path
        self.csv_path = csv_path
        self.records: Dict[str, dict] = {}
        
        # Ensure data folder exists
        os.makedirs(os.path.dirname(self.json_path), exist_ok=True)
        self.load_from_json()

    # --- File Handling & Exception Handling ---
    def load_from_json(self) -> None:
        """Load student records from JSON file with exception handling."""
        try:
            if not os.path.exists(self.json_path):
                self.records = {}
                return
            with open(self.json_path, mode="r", encoding="utf-8") as f:
                self.records = json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            print(f"[Warning] Failed to read JSON file ({e}). Starting with empty records.")
            self.records = {}

    def save_to_json(self) -> None:
        """Write records to JSON safely using try-finally."""
        file_obj = None
        try:
            file_obj = open(self.json_path, mode="w", encoding="utf-8")
            json.dump(self.records, file_obj, indent=4)
        except OSError as e:
            print(f"[Error] Could not save records to disk: {e}")
        finally:
            if file_obj:
                file_obj.close()

    def export_to_csv(self) -> None:
        """Export current records into a CSV file."""
        if not self.records:
            raise ValueError("No records to export.")

        fieldnames = ["student_id", "name", "course", "gpa"]
        with open(self.csv_path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.records.values())

    # --- CRUD Operations ---
    def add_student(self, student_id: str, name: str, course: str, gpa: float) -> None:
        if student_id in self.records:
            raise DuplicateStudentError(f"Student ID '{student_id}' already exists.")
        
        self.records[student_id] = {
            "student_id": student_id,
            "name": name.strip(),
            "course": course.strip(),
            "gpa": gpa,
        }
        self.save_to_json()

    def get_student(self, student_id: str) -> dict:
        if student_id not in self.records:
            raise StudentNotFoundError(f"Student ID '{student_id}' not found.")
        return self.records[student_id]

    def update_student(self, student_id: str, name: Optional[str] = None, 
                       course: Optional[str] = None, gpa: Optional[float] = None) -> None:
        student = self.get_student(student_id)
        if name:
            student["name"] = name.strip()
        if course:
            student["course"] = course.strip()
        if gpa is not None:
            student["gpa"] = gpa
            
        self.save_to_json()

    def delete_student(self, student_id: str) -> None:
        if student_id not in self.records:
            raise StudentNotFoundError(f"Student ID '{student_id}' not found.")
        del self.records[student_id]
        self.save_to_json()

    # --- Demonstrating Comprehensions & Lambdas ---
    def filter_honor_roll(self, min_gpa: float = 8.5) -> List[dict]:
        """List comprehension filtering students by minimum GPA."""
        return [s for s in self.records.values() if s["gpa"] >= min_gpa]

    def get_sorted_by_gpa(self, descending: bool = True) -> List[dict]:
        """Demonstrates lambda function usage for custom sorting."""
        return sorted(self.records.values(), key=lambda s: s["gpa"], reverse=descending)