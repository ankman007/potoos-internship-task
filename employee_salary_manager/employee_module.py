from __future__ import annotations

class Employee:
    def __init__(self, emp_id: int, name: str, salary: float):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.bonus = 0.0

    def apply_bonus(self, percentage: float) -> float:
        self.bonus = self.salary * (percentage / 100)
        final_salary = self.salary + self.bonus
        return final_salary

    def to_dict(self) -> dict:
        return {
            "id": self.emp_id,
            "name": self.name,
            "salary": self.salary,
            "bonus": self.bonus
        }