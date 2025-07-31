import re


# This regex matches a phone number in the format ddd-ddd-dddd
# where d is a digit, and allows for optional separators like '-', '.', or whitespace.

phoneRegex = re.compile(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b')