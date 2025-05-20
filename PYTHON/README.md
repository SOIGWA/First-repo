# 🎓 High School Grade System

A simple Python script that classifies U.S. high school students based on their grade level input. This beginner-friendly project is ideal for those learning about conditional statements in Python.

## 📋 Description

This program prompts the user to input a grade level (9–12) and outputs the corresponding student classification:

- Grade 9 → Freshman  
- Grade 10 → Sophomore  
- Grade 11 → Junior  
- Grade 12 → Senior  

If the input doesn't match any of these grades, the program outputs `TBD` (To Be Determined).

## 🧠 Concepts Covered

- `print()` statements
- `input()` function
- Type conversion (`int`)
- Conditional logic using `if`, `elif`, and `else`

## 💡 How It Works

1. The user is asked to input a number representing their grade.
2. The input is converted from a string to an integer.
3. The program checks the grade and prints the corresponding classification.
4. If the grade isn't 9, 10, 11, or 12, it returns "TBD".

## 🛠️ Usage

To run the script:

```bash
python3 high_school_grades.py
