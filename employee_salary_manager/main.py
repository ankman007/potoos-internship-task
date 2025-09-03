from salary_utils import fetch_employees, post_salary_update

def main():
    BONUS_PERCENTAGE = 10  

    print("Fetching employee data...")
    employees = fetch_employees()

    if not employees:
        print("No employees found or an error occurred. Exiting.")
        return

    updated_employees = []
    print("\n--- Salary Report ---")

    for emp in employees:
        final_salary = emp.apply_bonus(BONUS_PERCENTAGE)
        print(f"{emp.name:<10} | Final Salary: {final_salary:,.2f}")
        updated_employees.append(emp)

    post_salary_update(updated_employees)
    print("\nProcess completed successfully.")

if __name__ == "__main__":
    main()