## Setup

To setup this project:
    1- First fork the repo
    2- Clone the repository to your local machine
    3- Enter the following command to install all external dependencies
        `pip3 install --editable .`
    4- Make a new branch to work on your issue of choice using `git checkout -b NAMEOFBRANCH`

# Usage

Usage can be found by typing ```urlChecker --help```

Used by typing in:

```urlChecker -f inputFile```

Check the version of the program by typing in:

```urlChecker -v```

To check a single url, type the following:

```urlChecker -u NAMEOFURL```

To see your output in a JSON format, type the following:

```urlChecker -j ```

This url machine function also allows you to check the telescope project and run this program using the 10
latest blog posts urls posted. Run telescope locally first, then, to check each url, type the following:

```urlChecker -t```

To run the program as written above, enter the following into your terminal


## Running the code formatter

The code formatter will be ran every time you save the file by default on VSCode.

You can also use the shell script `code-formatter.sh` to run the "black" formatter to format your files


## Running the linter

The code linter will be ran every time you save the file by default on VSCode.

You can also use the shell script `py-linter-checker.sh` to run the "pylint" checker to ensure your files are styled correctly.

## Making a Pull Request

When you finish working on your issue, ensure you test your code to ensure it's ready to be committed.
Afterwards, commit, push to your remote branch, and make a PR explaining what you did, does it work and include a screenshot if applicable.