from pprint import pprint
from operator import itemgetter

faculty_dict = { 'Ellenberg': [\
              ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
              ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']
                            ],
              'Li': [\
              ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
              ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
              ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
                            ]
            }

print(len(faculty_dict))
faculty_list = list(faculty_dict.items())
pprint(faculty_list[:3])


professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
                ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],\
                ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
                ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
                ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
            }

print(len(professor_dict))
prof_list = []
for key in sorted(professor_dict.keys(), key=itemgetter(1,0)):
    prof_list.append([key, professor_dict[key]])

pprint(prof_list[:3])
