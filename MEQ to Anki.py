# Anki generator goddamn which fking version am I up to

# Use cloze generators
# regex to separate out headings
# each card is a heading 
# above headings are considered tags


# generate IDs

regex_statement = "#+ (.+)"

# algorithm to identify subcards
# eg. 1 2 3 4 4 3 4 4 2 3 3. 4 4 4 4 3 3 should be cards
# likely manage as a queue, consider tuples with line numbers if required
# note edge case of the end
# ignore keywords including references
# custom tags