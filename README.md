# Linux User Automation

This automation project simplifies the process of adding multiple users to a Linux system. It utilizes Python for automation and includes scripts to generate random names, convert input data, and create Linux users.

## Prerequisites

Before running the scripts, make sure to:

1. Run `requirements.py` to install necessary dependencies.

2. Use the provided `input.xlsx` for practice. If using a different file, either rename it to 'input' or update the filename in all Python scripts accordingly.

3. If desired, use `Faker.py` to generate random names. Edit the code to specify the number of names you want.

## Usage

1. Copy the generated names into the `input.xlsx` file.

2. Run `excel.py` to convert the input into the desired format for Linux users (/etc/passwd).

3. For advanced output, run `advexcel.py`.

4. To convert the Excel file into text format, run `txtconv.py`.

## Files in the Repository

1. `Faker.py`: Python script to generate random names.

2. `README.md`: This file, providing instructions and information about the project.

3. `advexcel.py`: Python script for advanced output.

4. `excel.py`: Python script to convert input into the desired format.

5. `input.xlsx`: Example input file for practice. Rename or update filenames in scripts if using a different file.

6. `requirements.txt`: File containing dependencies. Install using `requirements.py`.

7. `txtconv.py`: Python script to convert Excel into text format.

## Contributing

If you have suggestions, find issues, or want to contribute, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](url) file for details.
