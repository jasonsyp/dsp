#The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.

import csv

class CSVParser(object):

    def __init__(self, data):
        self.data = data

    def read_data(self):
         with open(self.data, 'r') as input_file:
             parsed_data = [row for row in csv.reader(input_file.read().splitlines())]
         return parsed_data

    def get_min_score_difference(self, parsed_data):
        parsed_data.pop(0)
        goals = [x[5] for x in parsed_data]
        goals_allowed = [x[6] for x in parsed_data]
        values = [int(x) - int(y) for x,y in zip(goals, goals_allowed)]
        return values.index(min(values))

    def get_team(self, index_value, parsed_data):
        teams = [x[0] for x in parsed_data]
        return teams[index_value]

if __name__ == '__main__':
    input_data = CSVParser('football.csv')
    formatted_data = input_data.read_data()
    min_index = input_data.get_min_score_difference(formatted_data)
    answer = input_data.get_team(min_index, formatted_data)
    print('The EPL team with the smallest goal differential is:', answer)
