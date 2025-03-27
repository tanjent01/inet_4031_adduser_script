# INET4031 Add Users Script and User List

## Program Description

This program is designed to automate the process of adding multiple users to a system. It takes an input file containing properly formatted users and user data, and automatically adds them and their respective data to the system, as well as assigns them to groups. Usually the adduser command would be used and data would have to be typed in manually. Also commands to add users to groups would have to be used. This program automates these.

## Program User Operation

The program first imports all necessary libraries, and sets up variables needed to determine if a user is to be added, as well as to split up the data into fields. The program then checks for the skip character as well as the appropriate format for user data. Data is then assigned to variables, paths to adduser commands are assigned to variables and ran. Print statements are included to keep track of where the code is at and to help with error catching.

### Input File Format

Each line represents a user. Each field represents username, password, last name, first name, and group or groups. Each field is separated by ":". If a user needs to be skipped, insert "#" at the start of the line. If a user should be added to no groups, put a "-" in the groups field.


### Command Execution

Ensure that create-users.py is executable. To run: ./create-users.py < <name of input file>


### "Dry Run"
