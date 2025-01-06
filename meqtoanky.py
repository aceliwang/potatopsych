# todo: ignore hr

import re
import uuid

class Card:
    def __init__(self, id, front, back, tags=[]):
        self.front = front
        self.back = [line.find("-")*"&nbsp;" + line for line in back]
        self.tags = tags
        self.id = id

    def __str__(self):
        return f"{self.id}|{"<br>".join(self.front).replace("#", "\#")}|{"<br>".join(self.back)}|{" ".join(self.tags)}"
    
class Heading:
    def __init__(self, level, line, content, comments=False):
        self.level = level
        self.line = line
        self.content = content
        self.tag = []
        self.go_ahead = True
        self.needs_id = True
        self.needs_tag = True
        self.comments=[]
        # PARSE COMMENTS
        if comments:
            comment_list = []
            for comment in comments[0].split(";"):
                directives = comment.split(":")
                match directives[0]:
                    case "tag":
                        self.needs_tag = False
                        self.tag.append(directives[1])
                    case "status":
                        if directives[1] == "incomplete": 
                            self.go_ahead = False
                        comment_list.append(comment)
                    case "id":
                        self.needs_id = False
                        self.id = directives[1]
                    case _:
                        comment_list.append(comment)
            self.comments = comment_list
        if self.needs_id: self.add_id()
        # if self.needs_tag: self.add_tag()

    def __str__(self):
        return self.new_heading()

    def add_id(self):
        self.id = str(uuid.uuid4())

    def add_tag(self):
        # strip the #s
        # stripping the rest of the comments
        if self.content.find("<!--") == -1:
            i = self.content[self.content.find(" ") + 1:]
        else:
            i = self.content[self.content.find(" ")+1:self.content.find("<!--")]

        print(self.content)
        self.tag.append(i.lower().strip().replace(" ", "-"))

    def new_heading(self):
        new_tag = ""
        if self.tag:
            new_tag = f'tag:{",".join(self.tag)};'
        
        return f'{self.content} <!-- {new_tag}id:{self.id}{";".join([""] + self.comments)} -->'
    




# open file
with open("meqanki.md") as file:
    content = file.readlines()

# manipulate file
content = [line for line in content if line != "\n"]
content = [line[:-1] for line in content if "\n" in line[-2:]]
old_content = content.copy()
print(f'{content=}')

# identify headings
headings_list = []
for line_number, line in enumerate(content):
    if line[0] != "#":
        continue
    heading_level = line.split(" ")[0].count("#")
    if line.find("<!--") == -1:
        line_without_comments = line.strip()
    else: 
        line_without_comments = line[:line.find("<!--")].strip() # includes the ###
    print(f'{line=} {line_without_comments=}')
    comments = re.findall("<!-- (.*) -->", line)
    headings_list.append(Heading(level=heading_level, line=line_number, content=line_without_comments, comments=comments))

# for line in headings_list:
#     print(line)

card_list = []

tag_stack = [headings_list[0]]
for i in range(len(headings_list) - 1):
    first = headings_list[i]
    second = headings_list[i+1]
    # print("comparing", first, second)
    
    if second.level <= first.level:
        # covers cases of second[0] == first[0] or second[0] < first [0]
        # first becomes a card
        # print("card made", first[2])
        tags = [heading.tag[0] for heading in tag_stack[:-1]] # eliminates starting headers
        all_the_headings_for_the_content = [heading.content for heading in tag_stack[:-1]] + [content[first.line]]
        print(f'{content=}')
        rest_of_content=content[first.line + 1:second.line]
        if first.go_ahead: card_list.append(Card(front=all_the_headings_for_the_content, back=rest_of_content, tags=first.tag + tags, id=first.id))


        for j in range(first.level - second.level + 1):
            tag_stack.pop()
    else:
        if not first.tag: first.add_tag()
    tag_stack.append(second)
    # print(stack)

print("CARDS\n\n")
for card in card_list:
    print(f'Card: {card}')

# algorithm to figure out cards 1 2 3a 4 3b 3c 4 2 3 4
# shuffle along 1 2: do nothing. add 1 to stack. stack = 1
# shuffle along 2 3a: do nothing. add 2 to stack. 1 2
# shuffle along 3a 4: do nothing. add 3a to stack. 1 2 3a
# shuffle along 4 3b: because 3 is less than 4, 4 needs to become a card. DIFFERENCE OF -1. POP 0. 1 2 3a.
# shuffle along 3b 3c: because 3 is same as 3, first 3b needs to become a card. DIFFERENCE of 0. delete previous 3a from stack (POP ONCE). add 3b to stack APPEND FIRST. 1 2 3b
# shuffle along 3c 4: do nothing. add 3c to stack. 1 2 3c
# shuffle along 4 2: because 2 is less than 4, 4 needs to become a card. DIFFERENCE OF 2. delete previous 2. 1 2 3c 4
# shuffle along 2 3
# shuffle along 3 4

for heading in headings_list:
    old_content[heading.line] = heading.new_heading()

with open("meqanki.md", "w") as file:
    for line in old_content:
        file.write(line)
        file.write("\n")

with open("anki.txt", "w") as file:
    file.write("#separator:Pipe\n")
    for card in card_list:
        file.write(card.__str__())
        file.write("\n")