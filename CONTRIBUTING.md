# Setup

To setup this project:
    1- First fork the repo
    2- Clone the repository to your local machine
    3- Enter the following command to install all external dependencies
        `pip install -r requirements.txt`
    4- Make a new branch to work on your issue of choice using `git checkout -b NAMEOFBRANCH`

## Usage

Usage can be found by typing ```UrlAutomationMachine -h```

To check a file of given urls, type the following:

```UrlAutomationMachine -f inputFile```

To check a single url, type the following:

```UrlAutomationMachine -u NAMEOFURL```

To see your output in a JSON format, type the following:

```UrlAutomationMachine -j```

This url machine function also allows you to check the telescope project and run this program using the 10
latest blog posts urls posted. Run telescope locally first, then, to check each url, type the following:

```UrlAutomationMachine -t```

## Running the code formatter

The code formatter will be ran every time you save the file by default on VSCode.

You can also use the shell script `code-formatter.sh` to run the "black" formatter to format your files

## Running the linter

The code linter will be ran every time you save the file by default on VSCode.

You can also use the shell script `py-linter-checker.sh` to run the "pylint" checker to ensure your files are styled correctly.

## Testing Coverage

This project utilizes the "pytest" module to create unit tests and test suites for the program. If you're planning on adding any new tests,
please put them in the "tests" folder. If you're planning on making a test suite, make a folder inside the tests folder and put your test suit there.

From the root folder of the project, type `pytest` in order to run the tests created.

## Making a Pull Request

When you finish working on your issue, ensure you test your code to ensure it's ready to be committed.
Afterwards, commit, push to your remote branch, and make a PR explaining what you did, does it work and include a screenshot if applicable.
