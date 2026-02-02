# Challenge 02: 🏭 Manufacture the toys

**Difficulty:** 🟢 Easy
**View:** [adventjs.dev/en/challenges/2025/2](https://adventjs.dev/en/challenges/2025/2)

## Instructions

Santa's factory has started to receive the toy **production list**. Each line indicates **which toy** must be manufactured and **how many units**.

The elves, as always, have messed things up: they wrote down some toys with quantities that don't make any sense.

You have a list of objects with this structure:

- `toy`: the name of the toy (string)
- `quantity`: how many units must be manufactured (number)

Your task is to write a function that takes this list and returns **an array of strings with**:

- Each toy **repeated as many times** as indicated by `quantity`.
- In the **same order** in which they appear in the original list.
- **Ignoring** toys with invalid quantities (less than or equal to 0, or not a number).

## 🧩 Examples

```javascript
const production1 = [
  { toy: 'car', quantity: 3 },
  { toy: 'doll', quantity: 1 },
  { toy: 'ball', quantity: 2 }
]
const result1 = manufactureGifts(production1)
console.log(result1) // ['car', 'car', 'car', 'doll', 'ball', 'ball']

const production2 = [
  { toy: 'train', quantity: 0 },
  { toy: 'bear', quantity: -2 },
  { toy: 'puzzle', quantity: 1 }
]
const result2 = manufactureGifts(production2)
console.log(result2) // ['puzzle']

const production3 = []
const result3 = manufactureGifts(production3)
console.log(result3)
// []
```

## Solution

<details hide>

<summary><h3>Spoiler</h3></summary>

``` python
def manufacture_gifts(gifts_to_produce):
    return [gift["toy"] for gift in gifts_to_produce for _ in range(gift["quantity"])]
```

</details>
