# Lab 6 Automatic Build using PyBuilder

Rita AbouFares

This project completes the graded calculator exercise (Exercise 1). The optional Makefile exercise is not included.

## Project files

```text
calculator_Rita_AbouFares/
    build.py
    requirements.txt
    README.md
    src/main/python/calculator_Rita_AbouFares/__init__.py
    tests/__init__.py
    tests/unittest/__init__.py
    tests/unittest/calculator_Rita_AbouFares/__init__.py
    tests/unittest/calculator_Rita_AbouFares/test_calculator_Rita_AbouFares.py
```

## Run from the existing lab6 folder

Open a PowerShell terminal in `lab6`. These commands use the local virtual environment without requiring an activation script:

```powershell
$env:Path = (Join-Path (Get-Location) '.venv\Scripts') + ';' + $env:Path
cd .\calculator_Rita_AbouFares
python -m unittest tests.unittest.calculator_Rita_AbouFares.test_calculator_Rita_AbouFares
pyb run_unit_tests
pyb
```

`pyb` runs the default `publish` task locally. It does not upload the project to Git, Moodle, or a package registry.

## Run after extracting the ZIP on another computer

Open PowerShell inside the extracted `calculator_Rita_AbouFares` directory, then run:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
$env:Path = (Join-Path (Get-Location) '.venv\Scripts') + ';' + $env:Path
python -m unittest tests.unittest.calculator_Rita_AbouFares.test_calculator_Rita_AbouFares
pyb run_unit_tests
pyb
```

Internet access is needed to install PyBuilder and its automatically managed build dependencies the first time.

## Verification

Verified with Python 3.14.0 and PyBuilder 0.13.24:

- The exact dotted `python -m unittest` command ran 7 tests and passed.
- `pyb run_unit_tests` executed 7 unit tests and reported `BUILD SUCCESSFUL`.
- `pyb` executed the default `publish` task, ran all 7 tests, created `target/dist/calculator_Rita_AbouFares-0.1`, and reported `BUILD SUCCESSFUL` in 12 seconds (12228 ms).

The division-by-zero assertion is included in `test_divide`, matching the handout, so there are 7 test methods covering 8 assertions.

## Comparison with the handout

- Reproduced the original `add`, `subtract`, `multiply`, and `divide` logic, including `ValueError("Cannot divide by zero.")`.
- Reproduced the original addition, subtraction, multiplication, division, and division-by-zero assertions in `TestCalculator`, using `unittest`.
- Added `modulus(x, y)` using `%`, `power(x, y)` using `**`, and `square_root(x)` using the standard library's `math.sqrt`. Added one simple test method for each.
- Kept `python.core`, `python.unittest`, and the handout's four properties in `initialize(project)`. Added module-level `name`, `version`, and `default_task` declarations following the [PyBuilder project descriptor documentation](https://pybuilder.readthedocs.io/en/latest/customizing-the-build.html), because PyBuilder needs project metadata before plugin initialization. This also gives the generated distribution the correct project name and version. The handout's `unittest_module` property is retained for fidelity; discovery is configured by the next two properties.
- Set `dir_source_unittest_python` to `tests/unittest/calculator_Rita_AbouFares` and `unittest_module_glob` to `test_*` so the handout's folder layout and filenames are actually discovered. The specific test folder also avoids a name collision between the `unittest` test directory and Python's `unittest` library. These properties follow the [PyBuilder unittest plugin documentation](https://pybuilder.io/documentation/plugins). The handout's sample PyBuilder output warns that no unit tests executed.
- Restored valid indentation and the Python identifiers `__init__.py`, `__file__`, `__name__`, and `__main__`. Used Rita AbouFares consistently instead of the example instructor name.
- Added empty `__init__.py` files in the test directories so the dotted unittest command works consistently.
- Did not run `pyb --start-project` over the completed files: the handout makes initialization conditional, and the generator would introduce files and plugins outside the requested configuration.

## Screenshot and Moodle submission

1. Review the calculator code and tests and make sure you understand each function.
2. In a terminal inside `calculator_Rita_AbouFares`, run `pyb run_unit_tests`.
3. Capture a genuine terminal screenshot showing the command, all 7 tests passing, `BUILD SUCCESSFUL`, the base directory ending in `calculator_Rita_AbouFares`, `Build finished at`, and `Build took`.
4. On Windows, use **Win+Shift+S** yourself and select the terminal. Widen the terminal and reduce its font size if the directory or summary is clipped. Save the screenshot as `Lab6_Rita_AbouFares_build.png`.
5. Upload `calculator_Rita_AbouFares.zip` and the screenshot to the Lab 6 Moodle submission. If Moodle only accepts one attachment, put both in one ZIP before uploading.
6. Complete Moodle's final submission step and verify its submitted status.

No terminal screenshot is included; capture it from the actual command output. The ZIP excludes virtual environments, caches, and generated build directories, which PyBuilder recreates when run.
