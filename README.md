# ezproxy-get-usernames

Parses ezproxy logs and outputs a csv file with 3 columns, log name, unique usernames per log, and list of usernames used.

DIRNAME = change to the location of your logs
REGEX = Change this regular expression to look for usernames. This default looks for letters 4-10 long followed by 2 digits.
