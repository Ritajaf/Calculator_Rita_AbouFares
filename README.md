# Lab 6 Automatic Build Using PyBuilder

**Student:** Rita AbouFares  
**Course:** EECE 435L  
**Project:** `calculator_Rita_AbouFares`  
**Version:** `0.1`

This project implements a Python calculator and uses PyBuilder to automate unit testing and creation of a local distribution. It completes the graded calculator exercise by adding modulus, exponentiation, and square root functions with unit tests. The optional Makefile exercise is not included.

## Project Structure

```text
calculator_Rita_AbouFares/
├── build.py
├── requirements.txt
├── README.md
├── src/
│   └── main/
│       └── python/
│           └── calculator_Rita_AbouFares/
│               └── __init__.py
└── tests/
    ├── __init__.py
    └── unittest/
        ├── __init__.py
        └── calculator_Rita_AbouFares/
            ├── __init__.py
            └── test_calculator_Rita_AbouFares.py
```

The GitHub repository contains these project files at its root, together with a `.gitignore` file. PyBuilder creates its dependency environments, reports, and distribution directories when the build runs.

## Calculator Functions

The calculator functions are defined in `src/main/python/calculator_Rita_AbouFares/__init__.py`.

| Function | Purpose | Example | Result |
| --- | --- | --- | --- |
| `add(x, y)` | Addition | `add(1, 2)` | `3` |
| `subtract(x, y)` | Subtraction | `subtract(5, 3)` | `2` |
| `multiply(x, y)` | Multiplication | `multiply(3, 4)` | `12` |
| `divide(x, y)` | Division | `divide(10, 2)` | `5.0` |
| `modulus(x, y)` | Remainder | `modulus(10, 3)` | `1` |
| `power(x, y)` | Exponentiation | `power(2, 3)` | `8` |
| `square_root(x)` | Square root using `math.sqrt` | `square_root(9)` | `3.0` |

`divide(x, y)` raises `ValueError("Cannot divide by zero.")` when `y` is zero. The modulus and power functions use Python's `%` and `**` operators, respectively.

## Requirements

The project was verified with Python **3.14.0** and PyBuilder **0.13.24**. The PyBuilder version is pinned in `requirements.txt`:

```text
pybuilder==0.13.24
```

The calculator uses Python's standard library. Internet access is needed to install PyBuilder and, on the first build, its automatically managed plugin dependencies.

## Setup

Open PowerShell in the project directory containing `build.py`. This can be the directory extracted from the submission ZIP or a local clone of the GitHub repository.

Create a virtual environment and install the required PyBuilder version:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Add the virtual environment's executables to the current PowerShell session:

```powershell
$env:Path = (Join-Path (Get-Location) ".venv\Scripts") + ";" + $env:Path
```

Run the following commands from the same project directory and PowerShell session. In a new session, repeat the command that updates `Path` before using `python` or `pyb`.

## Run Unit Tests

Run the tests through PyBuilder:

```powershell
pyb run_unit_tests
```

A successful run reports:

```text
Executed 7 unit tests
All unit tests passed.
...
BUILD SUCCESSFUL
```

The same tests can also be run directly with Python:

```powershell
python -m unittest -v tests.unittest.calculator_Rita_AbouFares.test_calculator_Rita_AbouFares
```

The test file contains seven test methods covering addition, subtraction, multiplication, division, modulus, exponentiation, and square root. The division test also checks that dividing by zero raises `ValueError`, giving eight assertions in total. All seven test methods passed during verification.

## Run the Full Build

Run PyBuilder without specifying a task:

```powershell
pyb
```

The default task is `publish`. In this project, it runs the configured build sequence, including unit testing and creation of the local distribution. The full build was verified successfully and produced the distribution directory:

```text
target/dist/calculator_rita_aboufares-0.1/
```

The `publish` task creates local build output. Uploading the project to GitHub or Moodle is a separate step.

## How the Build Is Automated

`build.py` loads the `python.core` and `python.unittest` plugins and defines the project name, version, and default task.

The unit test configuration points PyBuilder to `tests/unittest/calculator_Rita_AbouFares` and selects modules matching `test_*`. This allows PyBuilder to discover the tests in the assignment's directory layout.

With this configuration, one command runs all unit tests, while the default build command also creates the distribution. PyBuilder manages the task sequence and reports whether the build succeeded or failed.
