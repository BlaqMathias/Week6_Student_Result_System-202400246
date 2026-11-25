# Week 6 Student Result Processing System

**Level 3 Software Engineering – Week 6 Practical**

## 1. Project Overview

The Student Result Processing System is a Python project that demonstrates modular programming, input validation, grading, result calculation, GPA calculation, automated testing, code review, refactoring and basic version control.

The program validates student details and assessment scores, calculates a total score, assigns a letter grade and grade point, and calculates GPA using course credit units.

The project uses the illustrative grading scale supplied in the Week 6 practical slides.

## 2. Project Objectives

The project is designed to:

- Validate student names and registration numbers.
- Check that assessment scores are valid and within their permitted ranges.
- Calculate a student's total score.
- Assign a letter grade and grade point.
- Calculate GPA using course credit units.
- Return result information in a structured form.
- Use automated tests to check program behaviour.
- Review and refactor poorly structured code.

## 3. Technologies Used

- **Python** – programming language.
- **Visual Studio Code** – code editor.
- **Git** – version control.
- **GitHub** – online repository hosting.
- **unittest** – Python's built-in automated testing framework.

No third-party Python package is required for the supplied routines.

## 4. Project File Structure

```text
Week6_Student_Result_System/
│
├── main.py
├── validation.py
├── grading.py
├── result_module.py
├── test_grading.py
├── test_result_module.py
├── README.md
│
└── Code_Review_and_Refactoring_Document.docx  (optional supporting document)
```

### What each file does

| File | Responsibility |
|---|---|
| `main.py` | Runs the sample application and displays a student's result and GPA. |
| `validation.py` | Checks student details and assessment scores. |
| `grading.py` | Stores the grading boundaries and calculates grades and grade points. |
| `result_module.py` | Calculates total scores, generates result records and calculates GPA. |
| `test_grading.py` | Tests the grading function with normal, boundary and invalid values. |
| `test_result_module.py` | Tests total score calculation, result generation and GPA calculation. |
| `README.md` | Explains the project, its files and how to run it. |

---

## 5. Explanation of the Code

### Code 1: Student Validation – `validation.py`

This file contains two functions that check whether information supplied to the system is valid.

#### A. `validate_student(name, registration_number)`

This function validates a student's identity details.

It checks that:

1. The student's name is text.
2. The name is not empty or made up only of spaces.
3. The registration number is text.
4. The registration number is not empty or made up only of spaces.

If the details are valid, the function returns `True`. If a value is invalid, it raises an appropriate error.

#### B. `validate_score(score, maximum, field_name)`

This function validates an assessment score.

It checks that:

1. The score is numeric (`int` or `float`).
2. The score is not a Boolean value (`True` or `False`).
3. The score is not below zero.
4. The score does not exceed the maximum allowed mark.

For example:

```python
validate_score(18, 20, "Assignment")
```

This is valid and returns `True`.

But:

```python
validate_score(25, 20, "Assignment")
```

raises a `ValueError` because the maximum assignment score is 20.

**In simple terms:** `validation.py` acts as the checkpoint of the application. It prevents invalid student details and scores from moving into result processing.

### Code 2: Grading Routines – `grading.py`

This file determines the letter grade and grade point for a student's total score.

#### A. `GRADE_BOUNDARIES`

The grading scale is stored as a list of tuples. Each tuple contains three values:

- Minimum score.
- Letter grade.
- Grade point.

The illustrative scale is:

| Score range | Grade | Grade point |
|---:|:---:|---:|
| 70–100 | A | 5 |
| 60–69 | B | 4 |
| 50–59 | C | 3 |
| 45–49 | D | 2 |
| 40–44 | E | 1 |
| 0–39 | F | 0 |

For example, `(70, "A", 5)` means that a score of at least 70 earns grade A and 5 grade points.

#### B. `calculate_grade(total_score)`

This function checks that the total score is numeric and between 0 and 100. It then loops through `GRADE_BOUNDARIES` and returns the correct letter grade.

#### C. `calculate_grade_point(total_score)`

This function performs the same type and range checks but returns the numerical grade point instead of the letter grade.

The loop:

```python
for minimum, grade, points in GRADE_BOUNDARIES:
```

uses **tuple unpacking**. For each tuple, Python assigns its first value to `minimum`, its second value to `grade`, and its third value to `points`. These are ordinary variable names, not special Python keywords.

Example:

```python
calculate_grade(87)        # Returns "A"
calculate_grade_point(87)  # Returns 5
```

**In simple terms:** `grading.py` is the grading table of the application. It automatically awards the correct grade and grade point based on the student's total.

### Code 3: Result Processing – `result_module.py`

This file brings validation and grading together to produce a student's result.

It imports functions from the other modules:

```python
from validation import validate_student, validate_score
from grading import calculate_grade, calculate_grade_point
```

#### A. `calculate_total_score(assignment, test, examination)`

This function validates the three assessment components and adds them together.

The maximum marks are:

- Assignment: 20.
- Test: 20.
- Examination: 60.

The maximum total is therefore 100.

For example:

```python
calculate_total_score(18, 17, 52)
```

returns `87`.

#### B. `generate_result(...)`

This function:

1. Receives the student's name, registration number, course code and assessment scores.
2. Validates the student's identity details.
3. Calls `calculate_total_score()` to validate and add the scores.
4. Calls `calculate_grade()` to determine the letter grade.
5. Calls `calculate_grade_point()` to determine the grade point.
6. Returns the information in a Python dictionary.

Example:

```python
result = generate_result(
    "John",
    "CSC/2026/001",
    "SWE 306",
    18,
    17,
    52
)

print(result)
```

The result contains the student's name, registration number, course code, total, grade and grade point.

**In simple terms:** `result_module.py` is the result calculator. It uses the validation and grading functions to turn assessment scores into a complete course result.

### Code 4: GPA Calculation – `result_module.py`

The `calculate_gpa(course_results)` function is added to the same `result_module.py` file, below `generate_result()`.

It calculates Grade Point Average using a weighted average. This means that each course's grade point is multiplied by its credit unit.

The function:

1. Checks that at least one course result was supplied.
2. Starts the weighted-point and credit-unit totals at zero.
3. Loops through the course records.
4. Retrieves each course's grade point and credit unit.
5. Checks that the grade point is between 0 and 5.
6. Checks that the credit unit is greater than zero.
7. Adds each grade point multiplied by its credit unit to the weighted total.
8. Adds the credit unit to the total units.
9. Divides the weighted points by the total credit units.

Example:

```python
courses = [
    {"grade_point": 5, "credit_unit": 3},
    {"grade_point": 4, "credit_unit": 2},
    {"grade_point": 3, "credit_unit": 3}
]

print(calculate_gpa(courses))
```

Calculation:

```text
Weighted points = (5 × 3) + (4 × 2) + (3 × 3)
                = 15 + 8 + 9
                = 32

Total credit units = 3 + 2 + 3
                   = 8

GPA = 32 / 8
    = 4.0
```

**In simple terms:** GPA calculation considers both the grade point and the credit unit of each course. A course with more credit units has a greater effect on the GPA.

### Code 5: Main Application – `main.py`

This is the file used to run the sample application.

It imports `generate_result()` and `calculate_gpa()` from `result_module.py`.

The `main()` function:

1. Supplies sample student details and assessment scores.
2. Calls `generate_result()` to process the student's result.
3. Loops through the returned dictionary and displays each result field.
4. Creates sample course records containing grade points and credit units.
5. Calls `calculate_gpa()` and displays the GPA rounded to two decimal places.

The condition:

```python
if __name__ == "__main__":
    main()
```

runs `main()` when `main.py` is executed directly. It prevents the main routine from automatically running just because another Python file imports it.

Run the application with:

```bash
python main.py
```

Expected sample values:

- Student: John
- Total score: 87
- Grade: A
- Grade point: 5
- Sample GPA: 4.0

**In simple terms:** `main.py` is the control centre. It brings the functions from the other files together and runs the sample workflow.

### Code 6: Grading Tests – `test_grading.py`

This file uses Python's built-in `unittest` framework to check whether `calculate_grade()` works correctly.

It contains four tests:

1. `test_grade_a_boundary()` checks that a score of 70 returns A.
2. `test_grade_b_boundary()` checks that a score of 60 returns B.
3. `test_grade_f()` checks that a score of 0 returns F.
4. `test_invalid_high_score()` checks that a score of 101 raises a `ValueError`.

For example:

```python
self.assertEqual(calculate_grade(70), "A")
```

means that the test expects `calculate_grade(70)` to return `"A"`.

The statement:

```python
with self.assertRaises(ValueError):
    calculate_grade(101)
```

checks that the function raises a `ValueError` for an invalid score.

**In simple terms:** `test_grading.py` acts like a checker. It tests whether the grading function gives the expected grades and rejects an invalid high score.

### Code 7: Result Module Tests – `test_result_module.py`

This file contains additional tests for the result-processing and GPA functions.

The tests are:

1. `test_calculate_total_score()` checks that scores of 18, 17 and 52 produce a total of 87.
2. `test_generate_result()` checks that the generated result contains total 87, grade A and grade point 5.
3. `test_calculate_gpa()` checks that the sample courses produce a GPA of 4.0.
4. `test_invalid_assignment_score()` checks that an assignment score of 25 is rejected because the maximum is 20.
5. `test_empty_course_results()` checks that an empty course list raises a `ValueError`.

**In simple terms:** `test_result_module.py` checks whether the application's result calculations and GPA calculations work correctly, including how it handles invalid information.

**Note:** The practical slides specify this test file as a required deliverable but do not provide its complete test implementation. The five tests above are additional tests written to cover the required result and GPA routines.

---

## 6. Code Review and Refactoring

### Code 8: Original Routine

The practical provides this original routine for review:

```python
def x(a, b, c, n):
    t = a + b + c
    if t >= 70:
        g = "A"
    elif t >= 60:
        g = "B"
    elif t >= 50:
        g = "C"
    else:
        g = "F"
    print(n, t, g)
    return t
```

The routine accepts three scores and a name, adds the scores, assigns a grade, prints the result and returns the total.

### Weaknesses identified

1. **Unclear function name:** `x()` does not explain the function's purpose.
2. **Unclear variable names:** `a`, `b`, `c`, `t` and `g` do not communicate what the values represent.
3. **No input validation:** It does not check whether the scores are numeric or within the permitted ranges.
4. **Incomplete grading scale:** It omits D and E from the grading scale supplied in the practical.
5. **Mixed responsibilities:** It calculates, grades and displays the result in one function.
6. **No documentation:** There is no docstring or explanation of the function.
7. **Difficult to test independently:** The calculation, grading and display operations are combined.

### What is refactoring?

Refactoring means improving the internal organisation of code without changing its intended behaviour.

A simple comparison is reorganising a long piece of writing into clear sections without changing its meaning.

### Refactoring workflow

The practical gives these steps:

1. Run the original routine and record its outputs.
2. Identify code smells and document the intended behaviour.
3. Extract one responsibility at a time.
4. Rename routines and variables to communicate intent.
5. Remove duplicated rules and centralise configuration.
6. Run automated tests after each meaningful change.
7. Compare outputs to confirm behaviour is preserved.

### Code 9: Refactored Routine

The following is an improved version that reuses the validation and grading functions already created:

```python
from validation import validate_score
from grading import calculate_grade, calculate_grade_point


def process_student_result(name, assignment, test, examination):
    validate_score(assignment, 20, "Assignment")
    validate_score(test, 20, "Test")
    validate_score(examination, 60, "Examination")

    total_score = assignment + test + examination

    grade = calculate_grade(total_score)
    grade_point = calculate_grade_point(total_score)

    return {
        "student_name": name,
        "total_score": total_score,
        "grade": grade,
        "grade_point": grade_point
    }
```

### Improvements made

- The function name `process_student_result()` clearly describes its purpose.
- Descriptive variable names make the code easier to understand.
- The scores are validated before calculation.
- The complete grading scale is reused from `grading.py`.
- Separate functions handle validation and grading.
- The result is returned as a dictionary rather than printed inside the processing function.

This refactored example can be saved in an additional file named `refactored_result.py`. It is a supporting example and does not replace any of the seven required files.

**Important distinction:** Refactoring should preserve intended behaviour. The original routine has an incomplete grading scale, so the improved version follows the full grading scale supplied by the practical. This corrects an identified weakness rather than preserving that incomplete grading behaviour.

---

## 7. How to Run the Project

### Requirements

- Python installed on your computer.
- Visual Studio Code or another Python editor.
- All project files saved in the same project folder.

### Run the main application

Open the terminal in the project folder and enter:

```bash
python main.py
```

The sample application should display John's result and the sample GPA.

### Run all automated tests

Enter:

```bash
python -m unittest -v
```

This discovers and runs the test files beginning with `test_`.

A successful test run displays `OK`. If a test fails, inspect the failure message, correct the issue and run the tests again.

---

## 8. Boundary-Value Testing

The practical recommends testing values around the permitted score range and grade transitions.

For a score range of 0–100, consider:

| Test value | Expected behaviour |
|---:|---|
| -1 | Invalid – below the minimum |
| 0 | Valid – minimum |
| 1 | Valid – just above minimum |
| 99 | Valid – just below maximum |
| 100 | Valid – maximum |
| 101 | Invalid – above maximum |

Also test the grade transitions:

- 39 and 40.
- 44 and 45.
- 49 and 50.
- 59 and 60.
- 69 and 70.

These tests help confirm that the grading boundaries are applied correctly.

---

## 9. Git Version Control

Git records changes made to the project. GitHub hosts the repository online so it can be accessed and shared.

From the project folder, initialise Git:

```bash
git init
```

Check the files:

```bash
git status
```

Stage the files:

```bash
git add .
```

Create a commit:

```bash
git commit -m "Create initial student result routines"
```

After making further improvements, stage and commit them with meaningful messages, for example:

```bash
git add .
git commit -m "Add automated tests and GPA calculation"
```

To upload the project to a GitHub repository, connect the local project to the repository and push the main branch:

```bash
git remote add origin https://github.com/YOUR-USERNAME/Week6_Student_Result_System.git
git branch -M main
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username and use the URL of the repository you actually created.

---

## 10. Project Conclusion

The Student Result Processing System demonstrates how a Python application can be divided into smaller routines with clear responsibilities.

The validation module checks student information and scores. The grading module assigns grades and grade points. The result module calculates totals, generates result records and calculates GPA. The main application coordinates the workflow, while the test files check that the routines behave as expected.

The code review identifies weaknesses in an original routine, and refactoring demonstrates how clearer names, validation, reusable functions and structured return values improve maintainability.

Overall, the practical demonstrates an iterative software engineering process: design, implement, review, test, refactor and manage changes with version control.
