import re
import glob
import os

DIRNAME = "logs"
REGEX = r"\b[a-zA-Z]{4,10}\d{2}\b" # Edit this regex for the pattern you want to look for, this default looks for letters 4-10 long followed by 2 digits


# create csv file with headings, logfile name, and username
outfile = open("usernames.csv", "w", encoding="utf-8")
outfile.write("filename,total unique usernames,username")

for filename in glob.glob(
    os.path.join(DIRNAME, "*.log")
):  # opens all log files in directory
    print("Now analyzing", filename)
    lines = [line.strip() for line in open(filename, encoding="utf8")]  # reads file

    username_list = []

    for line in lines:
        username = re.findall(REGEX, line)
        # if username isn't empty, print it
        if username:
            if username[0] not in username_list:
                username_list.append(username[0])

    # print to usernames.csv the name of the logfile and the usernames found in it,
    # all usernames in a single line, single column
    outfile.write("\n" + filename + "," + str(len(username_list)))
    FINAL_USERNAME_LIST = ""
    for username in username_list:
        FINAL_USERNAME_LIST += username + " "
    outfile.write("," + FINAL_USERNAME_LIST)