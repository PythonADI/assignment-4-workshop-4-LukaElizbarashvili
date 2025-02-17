# Task 1
names = ["Alice", "Bob", "Charlie", "David"]
for name in names:
    print(name)

# Task 2
for name in names:
    print(f"Hello, {name}! Hope you're having a great day.")
# Task 3
transportations = ["BMW", "Yamaha motorcycle", "Boeing jet"]
for transport in transportations:
    print(f"I would like to own a {transport}.")

# Task 4
guests = ["Albert Einstein", "Nikola Tesla", "Leonardo da Vinci"]
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner at my place.")

# Task 5
print(f"Unfortunately, {guests[1]} can't make it to the dinner.")
guests[1] = "Isaac Newton"
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner at my place.")

# Task 6
print("Great news! I found a bigger dinner table.")
guests.insert(0, "Marie Curie")
guests.insert(2, "Galileo Galilei")
guests.append("Charles Darwin")
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner at my place.")

# Task 7
print("Unfortunately, the new table won’t arrive in time, and I can invite only two people.")
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner.")
for guest in guests:
    print(f"{guest}, you’re still invited!")
del guests[:]
print("Final guest list:", guests)

# Task 8
places = ["Japan", "Norway", "New Zealand", "Switzerland", "Canada"]
print("Original list:", places)
print("Alphabetical order:", sorted(places))
print("Original order after sorted():", places)
print("Reverse alphabetical order:", sorted(places, reverse=True))
print("Original order after sorted(reverse=True):", places)
places.reverse()
print("Reversed order:", places)
places.reverse()
print("Back to original order:", places)
places.sort()
print("Sorted in alphabetical order:", places)
places.sort(reverse=True)
print("Sorted in reverse alphabetical order:", places)

# Task 9
print(f"Number of people invited to dinner: {len(guests)}")


