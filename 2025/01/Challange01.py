'''
Challenge #1: 🎁 Filter the defective gifts

Santa has received a list of gifts, but some are defective. A gift is defective if its name contains the # character.

Help Santa by writing a function that takes a list of gift names and returns a new list that only contains the non-defective gifts.

Examples

const gifts1 = ['car', 'doll#arm', 'ball', '#train']
const good1 = filterGifts(gifts1)
console.log(good1)
// ['car', 'ball']

const gifts2 = ['#broken', '#rusty']
const good2 = filterGifts(gifts2)
console.log(good2)
// []

const gifts3 = []
const good3 = filterGifts(gifts3)
console.log(good3)
// []
'''

def filter_gifts_original(gifts):
  valid_gifts = []
  for gift in gifts:
    if '#' not in gift:
      valid_gifts.append(gift)

  return valid_gifts

def filter_gifts(gifts):
    return [gift for gift in gifts if '#' not in gift]

# Main program
gifts1 = ['car', 'doll#arm', 'ball', '#train']
gifts2 = ['#broken', '#rusty']
gifts3 = []

print(filter_gifts(gifts1))
print(filter_gifts(gifts2))
print(filter_gifts(gifts3))