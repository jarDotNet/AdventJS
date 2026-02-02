'''
Challenge #14: 🗃️ Find the gift path

At the North Pole, the elves have simplified their storage system to avoid mistakes.
They now keep the presents in a magical object with limited depth, where each value appears only once.

Santa needs a quick way to know which path of keys he must follow to find a specific present.

Your task is to write a function that, given an object and a value, returns the array of keys that must be traversed to reach that value.

Rules:

- The object has at most 3 levels of depth.
- The value to search for appears at most once.
- The object only contains other objects and primitive values (strings, numbers, booleans).
- If the value does not exist, return an empty array.

Examples:

const workshop = {
  storage: {
    shelf: {
      box1: 'train',
      box2: 'switch'
    },
    box: 'car'
  },
  gift: 'doll'
}

findGiftPath(workshop, 'train')
// ➜ ['storage', 'shelf', 'box1']

findGiftPath(workshop, 'switch')
// ➜ ['storage', 'shelf', 'box2']

findGiftPath(workshop, 'car')
// ➜ ['storage', 'box']

findGiftPath(workshop, 'doll')
// ➜ ['gift']

findGiftPath(workshop, 'plane')
// ➜ []
'''

def find_gift_path_original(workshop: dict, gift: str | int | bool) -> list[str]:
  current_path = []

  for key, value in workshop.items():
      if value == gift:
        current_path.append(key)
        break
      elif isinstance(value, dict):
        current_path.append(key)
        path = find_gift_path_original(value, gift)
        if path:
           current_path += path
        else:
            current_path = []

  return current_path

def find_gift_path(workshop: dict, gift: str | int | bool) -> list[str]:
    for key, value in workshop.items():
        if value == gift:
            return [key]
        
        if isinstance(value, dict):
            path = find_gift_path(value, gift)
            if path:
                return [key] + path
    
    return []

# Main program
workshop = {
  "storage": {
    "shelf": {
      "box1": 'train',
      "box2": 'switch'
    },
    "box": 'car'
  },
  "gift": 'doll'
}

print(find_gift_path(workshop, "train"))
print(find_gift_path(workshop, "switch"))
print(find_gift_path(workshop, "car"))
print(find_gift_path(workshop, "doll"))
print(find_gift_path(workshop, "plane"))
