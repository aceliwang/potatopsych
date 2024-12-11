# open file
with open("meqankitesting.md") as file:
    content = file.readlines()

# manipulate file
content = [line for line in content if line != "\n"]
# print(content)

# identify headings
headings_array = []
for line_number, line in enumerate(content):
    if line[0] != "#":
        continue
    heading_level = line.split(" ")[0].count("#")
    headings_array.append((heading_level, line_number, line))


for line in headings_array:
    print(line)
print('hi')

# algorithm to figure out cards 1 2 3 4 3 3 4 2 3 4

# shuffle along 1 2: do nothing 
# shuffle along 2 3: do nothing
# shuffle along 3 4: do nothing
# shuffle along 4 3: because 3 is less than 4, 4 needs to become a card
# shuffle along 3 3: because 3 is same as 3, first 3 needs to become a card
# shuffle along 3 4: do nothing
# shuffle along 4 2: because 2 is less than 4, 4 needs to become a card
# shuffle along 2 3
# shuffle along 3 4