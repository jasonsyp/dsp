import re
import csv
from collections import Counter


csv_file = open('faculty.csv', 'r')
input_file = csv.reader(csv_file)
next(csv_file, None)

faculty_degrees = []
titles_list = []
email_list = []
domain_list = []

# Create lists from csv file; Use regular expression to search for e-mail address
email_pattern = re.compile('([\w\.-]+@[\w\.-]+)')
for row in input_file:
    faculty_degrees.append(row[1])
    titles_list.append(row[2])
    for match in email_pattern.findall(row[3]):
        email_list.append(match)

# strip leading and trailing spaces and split on spaces between degrees
split_degrees = []
for d in faculty_degrees:
    d.strip()
    split_degrees.extend(d.split())

# remove the periods from the degrees, so all degrees are spelled the same
final_degrees = []
for s in split_degrees:
    new_s = re.sub('[\.]', '', s)
    final_degrees.append(new_s)

# remove the lowercase supporting words, i.e. of/in/etc., from the titles
titles_list = [' '.join(word for word in i.split() if not word.islower()) for i in titles_list]

# search for the different domains in the e-mail addresses
for e in email_list:
    match = re.search(r'@.+', e)
    if match:
        domain_list += [match.group()]

# convert lists to sets to calculate unique values, use Counter to find frequencies
print('There are', len(set(final_degrees)), 'different degrees.')
print('The frequency of each degree is:', Counter(final_degrees))
print('There are', len(set(titles_list)), 'different titles.')
print('The frequency of each title is:', Counter(titles_list))
print(email_list)
print('There are', len(set(domain_list)), 'different e-mail domains.')
print(set(domain_list))

# Write e-mail list to a csv faculty_titles
output_file = open('emails.csv', 'w')
write_file = csv.writer(output_file, lineterminator='\n')
for row in email_list:
    write_file.writerow([row])
output_file.close()
