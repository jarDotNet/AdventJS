'''
Challenge #3: 👶 Help the intern

In Santa’s workshop there’s an intern elf who is learning to wrap gifts 🎁.

They’ve asked the elf to wrap boxes using only text… and they do it more or less correctly.

They are given two parameters:

- size: the size of the square gift
- symbol: the character the elf uses to make the border (when they don’t mess it up 😅)

The gift must meet these requirements:

- It must be a size x size square.
- The inside is always empty (filled with spaces), because the elf “doesn’t know how to draw the filling yet”.
- If size < 2, return an empty string: the elf tried, but the gift got lost.
- The final result must be a string with newline characters \n.

Yes, it’s an easy challenge… but we don’t want the intern to get fired. Right?

🧩 Examples
const g1 = drawGift(4, '*')
console.log(g1)
/*
 ****
 *  *
 *  *
 ****
 */

const g2 = drawGift(3, '#')
console.log(g2)
/*
###
# #
###
*/

const g3 = drawGift(2, '-')
console.log(g3)
/*
--
--
*/

const g4 = drawGift(1, '+')
console.log(g4)
// ""  poor intern…
'''

def draw_gift_original(size, symbol):
  draw = ""
  if size > 1:
    gap = size - 2
    draw = (symbol * size) + "\n"
    for _ in range(gap):
        draw += symbol + (" " * gap) + symbol + "\n"
    draw += (symbol * size) + "\n"
  return draw

def draw_gift(size, symbol):
    if size < 2:
        return ""
    
    gap = size - 2
    top_bottom = symbol * size
    middle = [symbol + (" " * gap) + symbol for _ in range(gap)]
    
    return "\n".join([top_bottom] + middle + [top_bottom])

# Main program
print(draw_gift(4, '*'))
print(draw_gift(3, '#'))
print(draw_gift(2, '-'))
print(draw_gift(1, '+'))