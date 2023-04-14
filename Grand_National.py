import random
import csv

# Load horses from CSV file
horse_file = 'horses.csv'
horses = []
with open(horse_file, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        horses.append(row[0])

# Load people from CSV file
people_file = 'people.csv'
people = []
with open(people_file, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        people.append(row[0])

# Randomly assign horses to people
horse_assignments = {}
random.shuffle(horses)
for person in people:
    horse = random.choice(horses)
    horse_assignments[person] = horse
    horses.remove(horse)

# Output results to text file
text_output_file = 'grand_national_draw.txt'
with open(text_output_file, 'w') as file:
    file.write('Family Grand National Draw\n')
    file.write('---------------------\n')
    for person, horse in horse_assignments.items():
        file.write(f'Person: {person}\n')
        file.write(f'Horse: {horse}\n')
        file.write('\n')

print(f'Results have been output to {text_output_file}.')