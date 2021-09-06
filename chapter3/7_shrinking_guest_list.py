guests = ['afiq', 'izzat', 'danial']
guests[0] = 'zaidan'
guests.insert(0, 'syafiq')
guests.insert(2, 'faiz')
guests.append('husnee')

print("I am very sorry, I can only invite two people for the dinner tomorrow")

cancel = guests.pop()
print(f"I am sorry {cancel.title()}, I can't invite you this time")
cancel = guests.pop()
print(f"I am sorry {cancel.title()}, I can't invite you this time")
cancel = guests.pop()
print(f"I am sorry {cancel.title()}, I can't invite you this time")
cancel = guests.pop()
print(f"I am sorry {cancel.title()}, I can't invite you this time")
print(f"Hye {guests[0].title()}, you are still invited for the dinner. Please come")
print(f"Hye {guests[1].title()}, you are still invited for the dinner. Please come")
del guests[1]
del guests[0]
print(guests)