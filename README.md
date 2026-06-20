# Basic Calculator

[![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg?logo=python)](https://www.python.org/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A modern, minimal command-line calculator written in Python — easy to read, easy to extend. Designed as a beginner-friendly example to demonstrate input handling, arithmetic operations, and simple CLI flow.

Highlights

- ✨ Clean, readable code with type hints and docstrings
- ➕ Basic arithmetic: addition, subtraction, multiplication, division
- 🛡️ Robust input validation and division-by-zero handling
- 🔁 Interactive loop: perform multiple calculations without restarting
- 📦 Zero external dependencies — runs on Python 3.6+

Demo

```text
$ python "basic calculator.py"
==================================================
         Welcome to the Simple Calculator!
==================================================
Enter the first number: 10
Enter the second number: 5

Select operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)

Enter choice (1/2/3/4): 1

10.0 addition 5.0 = 15.0

Do you want to perform another calculation? (yes/no): no
Thank you for using the calculator. Goodbye!
```

Quick start

1. Clone the repository

```bash
git clone https://github.com/Abu-Bakar-Rakib/Basic-calculator.git
cd Basic-calculator
```

2. Run the program

```bash
python "basic calculator.py"
```

Project structure

```
Basic-calculator/
├── README.md
└── basic calculator.py
```

How it works (brief)

- The program prompts for two numbers and an operation choice.
- Input validation ensures non-numeric input is rejected and division by zero is handled gracefully.
- The calculation is shown and the user can choose to continue or exit.

Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/name`)
3. Commit your changes (`git commit -m "Add feature"`)
4. Push to the branch (`git push origin feature/name`)
5. Open a pull request

If you make changes, please keep the code style simple and add comments or docstrings for new functions.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Author

Abu-Bakar-Rakib — https://github.com/Abu-Bakar-Rakib

