// # Anki generator goddamn which fking version am I up to

// # Use cloze generators
// # regex to separate out headings
// # each card is a heading 
// # above headings are considered tags


// # generate IDs

// find all headings
let regex_statement = RegExp('(#+) (.+)', 'g');
let heading_list;

while ((regex_match = regex_statement.exec(file_content)) !== null) {
    console.log(`Found ${regex_match[0]} at ${regex_match['index']}. Groups include ${regex_match['groups']}`)
    console.log(`Found ${regex_match[0]}. Next starts at ${regex_statement.lastIndex}`)
}


function identifyCards() {
    let length = heading_list.length // 0 1 2 (length is 3)
    for (let i = 0; i < (length - 1); i++ ){ 
        first = heading_list[i]
        second = heading_list[i + 1]
        if (second == first) {
            generate_card(first)
        } else if (second < first) {
            generate_card(first) 
        }
    }

}


// # algorithm to identify subcards
// # eg. 1 2 3 4 4 3 4 4 2 3 3. 4 4 4 4 3 3 should be cards
// # likely manage as a queue, consider tuples with line numbers if required
// # note edge case of the end
// # ignore keywords including references
// ignore any cards with no content
// # custom tags