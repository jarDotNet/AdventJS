'''
Challenge #8: 🎁 Find the unique toy

Santa 🎅 wants to know what the first non-repeated letter is in a toy's name 🎁.

Write a function that takes a string and returns the first letter that is not repeated, ignoring uppercase and lowercase when counting, but returning the letter as it appears in the string.

If there is none, return an empty string ("").

Examples:

findUniqueToy('Gift') // 'G'
// ℹ️ The G is the first letter that is not repeated
// and we return it exactly as it appears

findUniqueToy('sS') // ''
// ℹ️ The letters are repeated, since it doesn't distinguish uppercase

findUniqueToy('reindeeR') // 'i'
// ℹ️ The r is repeated (even if it's uppercase)
// and the e as well, so the first one is 'i'

// More cases:
findUniqueToy('AaBbCc') // ''
findUniqueToy('abcDEF') // 'a'
findUniqueToy('aAaAaAF') // 'F'
findUniqueToy('sTreSS') // 'T'
findUniqueToy('z') // 'z'
'''

def find_unique_toy_original(toy: str) -> str:
  normalized_toy = toy.casefold()

  for index, character in enumerate(toy):
    normalized_character = character.casefold()
    if index == 0 and normalized_toy.find(normalized_character, index + 1) == -1:
      return character
    elif index + 1 == len(toy) and normalized_toy.find(normalized_character, 0, index) == -1:
       return character
    elif normalized_toy.find(normalized_character, 0, index) == -1 and normalized_toy.find(normalized_character, index + 1) == -1:
      return character
  return ""

def find_unique_toy(toy: str) -> str:
    normalized_toy = toy.casefold()

    char_count = {}
    for char in normalized_toy:
        char_count[char] = char_count.get(char, 0) + 1

    for char in toy:
        if char_count[char.casefold()] == 1:
            return char

    return ""

# Main program
print(find_unique_toy('Gift'))
print(find_unique_toy('sS'))
print(find_unique_toy('reindeeR'))
print(find_unique_toy('AaBbCc'))
print(find_unique_toy('abcDEF'))
print(find_unique_toy('aAaAaAF')) 
print(find_unique_toy('sTreSS'))
print(find_unique_toy('z'))