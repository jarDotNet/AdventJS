'''
Challenge #24: 🪞 Check if trees are magical mirrors

At the North Pole, the elves have two magical binary trees that generate energy 🌲🌲 to keep the Christmas star ⭐️ shining. However, for them to work properly, the trees must be in perfect sync like mirrors 🪞.

Two binary trees are mirrors if:

- The roots of both trees have the same value.
- Each node of the first tree must have its corresponding node in the opposite position in the second tree.

And the tree is represented with three properties value, left, and right. The latter two display the remaining branches (if any):

const tree = {
  value: '⭐️',
  left: {
    value: '🎅'
    // left: {...}
    // right: { ... }
  },
  right: {
    value: '🎁'
    // left: { ... }
    // right: { ...&nbsp;}
  }
}
Santa needs your help to verify if the trees are synchronized so that the star can keep shining. You must return an array where the first position indicates if the trees are synchronized and the second position returns the value of the root of the first tree.

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
  tree1          tree2
   🎄              🎄
   / \             / \
 ⭐  🎅         🎅  ⭐
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
'''

def is_trees_synchronized_original(tree1, tree2):
    root1 = tree1["value"]
    root2 = tree2["value"]
    synchronized = root1 == root2

    if synchronized:
        left1, left2 = tree1.get("left", {}).get("value", None), tree2.get("left", {}).get("value", None)
        right1, right2 = tree1.get("right", {}).get("value", None), tree2.get("right", {}).get("value", None)
        if left1 and left2:
            synchronized = (left1 == right2) and (right1 == left2) 

    return [synchronized, root1]

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

# Main program
tree1 = {
  "value": '🎄',
  "left": { "value": '⭐' },
  "right": { "value": '🎅' }
}

tree2 = {
  "value": '🎄',
  "left": { "value": '🎅' },
  "right": { "value": '⭐' }
}

print(is_trees_synchronized(tree1, tree2))

tree3 = {
  "value": '🎄',
  "left": { "value": '🎅' },
  "right": { "value": '🎁' }
}

print(is_trees_synchronized(tree1, tree3))

tree4 = {
  "value": '🎄',
  "left": { "value": '⭐' },
  "right": { "value": '🎅' }
}

print(is_trees_synchronized(tree1, tree4))

print(is_trees_synchronized(
  { "value": '🎅' },
  { "value": '🧑‍🎄' }
))

  