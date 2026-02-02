'''
Challenge #7: 🎄 Decorating the tree

It’s time to decorate the Christmas tree 🎄! Write a function that receives:

- height → the height of the tree (number of rows).
- ornament → the ornament character (for example, "o" or "@").
- frequency → how often (in asterisk positions) the ornament appears.

The tree is drawn with asterisks *, but every frequency positions, the asterisk is replaced by the ornament.

The position counting starts at 1, from the top to the bottom, left to right. If frequency is 2, the ornaments appear in positions 2, 4, 6, etc.

The tree must be centered and have a one-line trunk # at the end.

🧩 Examples

drawTree(5, 'o', 2)
//     *
//    o*o
//   *o*o*
//  o*o*o*o
// *o*o*o*o*
//     #

drawTree(3, '@', 3)
//   *
//  *@*
// *@**@
//   #

drawTree(4, '+', 1)
//    +
//   +++
//  +++++
// +++++++
//    #
'''

def draw_tree(height, ornament, frequency):
    max_width =  height + (height - 1)
    num_ornaments = 0
    tree = []

    for line in range(1, height + 1):
        row_width = 2 * line - 1
        row_spaces = ((max_width - row_width) // 2) 
        row = (
            " " * row_spaces
            + "".join(
                ornament if ((num_ornaments + index) % frequency) == 0 else "*" for index in range(1, row_width + 1)
            )  
        )
        num_ornaments += len(row) - row_spaces
        tree.append(row)

    trunk = (" " * (max_width // 2)) + '#'

    return "\n".join(tree + [trunk])

# Main program
print(draw_tree(5, 'o', 2))
print(draw_tree(3, '@', 3))
print(draw_tree(4, '+', 1))