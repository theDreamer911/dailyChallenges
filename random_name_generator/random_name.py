import names

print("Full Names")
for i in range(10):
    print(names.get_full_name())

print("\nMale Names")
for i in range(5):
    print(names.get_full_name(gender='male'))

print("\nFemale Names")
for i in range(5):
    print(names.get_full_name(gender='female'))

print("\nFirst Names")
for i in range(10):
    print(names.get_first_name())

