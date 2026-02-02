# Challenge 08: 🎁 Find the unique toy

**Difficulty:** 🟢 Easy
**View:** [adventjs.dev/en/challenges/2025/8](https://adventjs.dev/en/challenges/2025/8)

## Instructions

Santa 🎅 wants to know what the first non-repeated letter is in a toy's name 🎁.

Write a function that takes a `string` and returns the **first letter that is not repeated**, ignoring uppercase and lowercase when counting, but returning the letter **as it appears** in the string.

If there is none, return an empty string ("").

## 🧩 Examples

```javascript
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
```

## Solution

<details hide>

<summary><h3>Spoiler</h3></summary>

``` python
def find_unique_toy(toy: str) -> str:
    normalized_toy = toy.casefold()

    char_count = {}
    for char in normalized_toy:
        char_count[char] = char_count.get(char, 0) + 1

    for char in toy:
        if char_count[char.casefold()] == 1:
            return char

    return ""
```

</details>
