#!/usr/bin/python3

# INET4031
# Tanner Jensen
# Date Created: 3/20/2025
# Date Last Modified: 3/27/2025

# os used for interacting with operating system, checking if user exists, adding user, configuring groups.
# re used for validating input data, ensures formats are followed.
# sys used for command line args like input filename and error catching.
import os
import re
import sys


def main():
    for line in sys.stdin:

        # Checks if # char is present in a given row (represents a user). # char is used to skip over a user when the program adds them one by one.
        match = re.match("^#",line)

        # Used to separate the characters in the file into the data being communicated. Each data attribute is separated by a ':'
        fields = line.strip().split(':')

	# Checks if match is true for a row (if the row starts with '#'), or if the number of data attributes (len(fields)) is something other than 5.
	# If either are true, user should be skipped and the program "continues', skipping adding the user and moving to the next user.
	# If both are false, that means the user is ready to be added and the continue command is skipped, allowing the program to finish adding the user.
        if match or len(fields) != 5:
            continue

	# These lines prepare the user data to be added to the system by assigning the data attributes parsed through previously to variables.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # This split separates a list of multiple groups that the user is to be added to, if more than one is listed.
        groups = fields[4].split(',')

        # Print statement to get output from the program and know where it is at. Helpful for error catching or tracking.
        print("==> Creating account for %s..." % (username))
        # cmd contains the path to the adduser command, using gecos to retrieve the username. User is added after the os call with no password.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        os.system(cmd)

        # Another print statement to track the programs progress and help with error tracking.
        print("==> Setting the password for %s..." % (username))
        # cmd contains the path to the command which adds the user's password to the user, giving them password functionality.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        os.system(cmd)

        for group in groups:
            #REPLACE THIS COMMENT with one that answers "What is this IF statement looking for and why? If group !='-' what happens?"
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                os.system(cmd)

if __name__ == '__main__':
    main()
