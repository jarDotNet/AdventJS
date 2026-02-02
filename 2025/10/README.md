# Challenge 10: 📨 Depth of Christmas magic

**Difficulty:** 🟢 Easy
**View:** [adventjs.dev/en/challenges/2025/10](https://adventjs.dev/en/challenges/2025/10)

## Instructions

**🎄 Depth of Christmas Magic.**

At the North Pole, Santa Claus is reviewing the magical letters 📩✨ he receives from children all over the world. These letters use an ancient Christmas language in which the brackets `[` and `]` represent the intensity of the wish.

The deeper the nesting of the brackets, the stronger the wish. Your mission is to find out the **maximum depth** at which the `[]` are nested.

But be careful! Some letters may be **poorly written**. If the brackets are not properly balanced (if one closes before it opens, there are extra closing brackets, or closing brackets are missing), the letter is invalid and you must return `1`.

## 🧩 Examples

```javascript
maxDepth('[]') // -> 1
maxDepth('[[]]') // -> 2
maxDepth('[][]') // -> 1
maxDepth('[[][]]') // -> 2
maxDepth('[[[]]]') // -> 3
maxDepth('[][[]][]') // -> 2

maxDepth('][') // -> -1 (closes before opening)
maxDepth('[[[') // -> -1 (missing closing brackets)
maxDepth('[]]]') // -> -1 (extra closing brackets)
maxDepth('[][][') // -> -1 (one remains unclosed)
```

## Solution

<details hide>

<summary><h3>Spoiler</h3></summary>

``` python
def max_depth(s: str) -> int:
    max_depth = 0
    current_depth = 0

    for char in s:
        if char == "[":
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif char == "]":
            current_depth -= 1
            if current_depth < 0: 
                return -1

    return max_depth if current_depth == 0 else -1
```

</details>
