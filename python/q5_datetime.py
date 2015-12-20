# Hint:  use Google to find python function

import datetime

####a)
date_start = '01-02-2013'
date_stop = '07-28-2015'

num_days = datetime.datetime.strptime(date_stop, '%m-%d-%Y') - datetime.datetime.strptime(date_start, '%m-%d-%Y')
print('The answer to a is:', num_days.days, 'days')

####b)
date_start = '12312013'
date_stop = '05282015'
num_days = datetime.datetime.strptime(date_stop, '%m%d%Y') - datetime.datetime.strptime(date_start, '%m%d%Y')
print('The answer to b is:', num_days.days, 'days')

####c)
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'
num_days = datetime.datetime.strptime(date_stop, '%d-%b-%Y') - datetime.datetime.strptime(date_start, '%d-%b-%Y')
print('The answer to c is:', num_days.days, 'days')
