'''
Challenge #6: 🧤 Matching gloves

In Santa's workshop, the elves have found a mountain of magical gloves in complete disarray. Each glove is described by two values:

- hand: indicates whether it is a left (L) or right (R) glove
- color: the color of the glove (string)

Your task is to help them match gloves: A valid pair is a left glove and a right glove of the same color.

You must return a list with the colors of all the pairs found. Keep in mind that there may be several pairs of the same color. The order is determined by whichever pair can be made first.

🧩 Examples

const gloves = [
  { hand: 'L', color: 'red' },
  { hand: 'R', color: 'red' },
  { hand: 'R', color: 'green' },
  { hand: 'L', color: 'blue' },
  { hand: 'L', color: 'green' }
]

matchGloves(gloves)
// ["red", "green"]

const gloves2 = [
  { hand: 'L', color: 'gold' },
  { hand: 'R', color: 'gold' },
  { hand: 'L', color: 'gold' },
  { hand: 'L', color: 'gold' },
  { hand: 'R', color: 'gold' }
]

matchGloves(gloves2)
// ["gold", "gold"]

const gloves3 = [
  { hand: 'L', color: 'red' },
  { hand: 'R', color: 'green' },
  { hand: 'L', color: 'blue' }
]

matchGloves(gloves3)
// []

const gloves4 = [
  { hand: 'L', color: 'green' },
  { hand: 'L', color: 'red' },
  { hand: 'R', color: 'red' },
  { hand: 'R', color: 'green' }
]

matchGloves(gloves4)
// ['red', 'green']
'''

from typing import List, Dict

def match_gloves(gloves: List[Dict[str, str]]) -> List[str]:
  not_paired = []
  paired_gloves = []

  for glove in gloves:
    pair_found = next(filter(lambda glv: glv.get("hand") != glove["hand"] and glv.get("color") == glove["color"], not_paired), None)
    if (pair_found):
      not_paired.remove(pair_found)
      paired_gloves.append(glove["color"])
    else:
      not_paired.append(glove)

  return paired_gloves

# Main program
gloves1 = [
  { "hand": 'L', "color": 'red' },
  { "hand": 'R', "color": 'red' },
  { "hand": 'R', "color": 'green' },
  { "hand": 'L', "color": 'blue' },
  { "hand": 'L', "color": 'green' }
]

gloves2 = [
  { "hand": 'L', "color": 'gold' },
  { "hand": 'R', "color": 'gold' },
  { "hand": 'L', "color": 'gold' },
  { "hand": 'L', "color": 'gold' },
  { "hand": 'R', "color": 'gold' }
]

gloves3 = [
  { "hand": 'L', "color": 'red' },
  { "hand": 'R', "color": 'green' },
  { "hand": 'L', "color": 'blue' }
]

gloves4 = [
  { "hand": 'L', "color": 'green' },
  { "hand": 'L', "color": 'red' },
  { "hand": 'R', "color": 'red' },
  { "hand": 'R', "color": 'green' }
]

print(match_gloves(gloves1))
print(match_gloves(gloves2))
print(match_gloves(gloves3))
print(match_gloves(gloves4))