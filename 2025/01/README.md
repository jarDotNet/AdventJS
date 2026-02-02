# Challenge 01: 🎁 Filter the defective gifts

**Difficulty:** 🟢 Easy

**View:** [adventjs.dev/en/challenges/2025/1](https://adventjs.dev/en/challenges/2025/1)

## Instructions

Santa has received a list of gifts, but some are **defective**. A gift is defective if its name contains the `#` character.

Help Santa by writing a function that takes a list of gift names and returns a new list that **only contains the non-defective gifts**.

## Examples

```javascript
const gifts1 = ['car', 'doll#arm', 'ball', '#train']
const good1 = filterGifts(gifts1)
console.log(good1) // ['car', 'ball']

const gifts2 = ['#broken', '#rusty']
const good2 = filterGifts(gifts2)
console.log(good2) // []

const gifts3 = []
const good3 = filterGifts(gifts3)
console.log(good3) // []
```

## Solution

<details hide>

<summary><h3>Spoiler</h3></summary>

``` python
def filter_gifts(gifts):
    return [gift for gift in gifts if '#' not in gift]
```

</details>
