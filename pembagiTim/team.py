import random
# people = ['John', 'Luke', 'Ben', 'Veronica', 'Daniel', 'Christian',
#           'Sean', 'Frank', 'Lucas', 'Jerome', 'Fiona', 'Sam']
people = ["Ian", "Kevin", "Carl", "Veronica", "Daniel",
          "Christian", "Sean", "Frank", "Phillip", "Fiona"]
number_people = len(people)
number_of_teams = 3

while number_people > 0 and number_of_teams > 0:
    team = random.sample(people, int(number_people/number_of_teams))

    for x in team:
        people.remove(x)
        number_people -= int(number_people/number_of_teams)
        number_of_teams -= 1
print(team)
