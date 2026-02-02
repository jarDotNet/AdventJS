# Challenge 24: 🪞 Check if trees are magical mirrors

**Difficulty:** 🟡 Medium
**View:** [adventjs.dev/en/challenges/2025/24](https://adventjs.dev/en/challenges/2025/24)

## Instructions

At the North Pole, the elves have **two magical binary trees that generate energy** 🌲🌲 to keep the Christmas star ⭐️ shining. However, for them to work properly, the trees must be in perfect sync **like mirrors** 🪞.

**Two binary trees are mirrors if:**

- The roots of both trees have the same value.
- Each node of the first tree must have its corresponding node in the opposite position in the second tree.

And the tree is represented with three properties: `value`, `left`, and `right`. The latter two display the remaining branches (if any):

```javascript
const tree1 = {
  value: '🎄',
  left: { value: '⭐' },
  right: { value: '🎅' }
}

const tree2 = {
  value: '🎄',
  left: { value: '🎅' }
  right: { value: '⭐' },
}

isTreesSynchronized(tree1, tree2) // [true, '🎄']

/*
  tree1           tree2
   🎄              🎄
   / \             /  \
 ⭐   🎅         🎅  ⭐
*/

const tree3 = {
  value: '🎄',
  left: { value: '🎅' },
  right: { value: '🎁' }
}

isTreesSynchronized(tree1, tree3) // [false, '🎄']

const tree4 = {
  value: '🎄',
  left: { value: '⭐' },
  right: { value: '🎅' }
}

isTreesSynchronized(tree1, tree4) // [false, '🎄']

isTreesSynchronized(
  { value: '🎅' },
  { value: '🧑‍🎄' }
) // [false, '🎅']
```

## Solution

<details hide>

<summary><h3>Spoiler</h3></summary>

``` python
def is_trees_synchronized(tree1, tree2):
    if not tree1 and not tree2:
        return [True, None]  
    
    if not tree1 or not tree2:
        return [False, tree1["value"] if tree1 else None] 

    if tree1["value"] != tree2["value"]:
        return [False, tree1["value"]]

    left_mirror, _ = is_trees_synchronized(tree1.get("left"), tree2.get("right"))
    right_mirror, _ = is_trees_synchronized(tree1.get("right"), tree2.get("left"))

    return [left_mirror and right_mirror, tree1["value"]]
```

</details>
