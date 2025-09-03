import json
import os
from typing import List

from employee_module import Employee

EMPLOYEES_FILE = "employees.json"

def fetch_employees() -> List[Employee]:
    if not os.path.exists(EMPLOYEES_FILE):
        print(f"Error: {EMPLOYEES_FILE} not found.")
        return []

    try:
        with open(EMPLOYEES_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            employees_data = data.get("employees", [])
            return [Employee(emp['id'], emp['name'], emp['salary']) for emp in employees_data]
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error reading or parsing {EMPLOYEES_FILE}: {e}")
        return []

def post_salary_update(updated_employees: List[Employee]):
    employees_dict_list = [emp.to_dict() for emp in updated_employees]    
    data_to_write = {"employees": employees_dict_list}

    try:
        with open(EMPLOYEES_FILE, 'w', encoding='utf-8') as f:
            json.dump(data_to_write, f, indent=2)
        print("\nSuccessfully updated employee salaries in employees.json.")
    except IOError as e:
        print(f"Error writing to {EMPLOYEES_FILE}: {e}")