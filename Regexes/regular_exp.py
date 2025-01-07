import re

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
mo1.group()

#named groups in regexes
pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
date_string = "2024-07-25"
match = re.match(pattern, date_string)
print("Year: ", match.group("year"))

xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans')
#['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 ladies']
