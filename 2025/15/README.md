# Challenge 15: ✏️ Drawing tables

**Difficulty:** 🟡 Medium
**View:** [adventjs.dev/en/challenges/2025/15](https://adventjs.dev/en/challenges/2025/15)

## Instructions

**ChatGPT has arrived at the North Pole** and the elf Sam Elfman is working on a gift and children management application.

To improve the presentation, he wants to create a `drawTable` function that receives an **array of objects** and turns it into a **text table**.

The drawn table must have:

- A header with column letters `A`, `B`, `C`…).
- The content of the table consists of the values of the objects.
- The values must be **left-aligned**.
- The fields always leave **one space on the left**.
- The fields leave on the right the space needed to align the box.

The function receives a second parameter `sortBy` that indicates the name of the field by which the **rows must be sorted**. The order will be **ascending alphabetical** if the values are strings and **ascending numeric** if they are numbers.

## 🧩 Examples

Check the examples to see how you should draw the table:

```javascript
drawTable(
  [
    { name: 'Charlie', city: 'New York' },
    { name: 'Alice', city: 'London' },
    { name: 'Bob', city: 'Paris' }
  ],
  'name'
)
// +---------+----------+
// | A       | B        |
// +---------+----------+
// | Alice   | London   |
// | Bob     | Paris    |
// | Charlie | New York |
// +---------+----------+

drawTable(
  [
    { gift: 'Book', quantity: 5 },
    { gift: 'Music CD', quantity: 1 },
    { gift: 'Doll', quantity: 10 }
  ],
  'quantity'
)
// +----------+----+
// | A        | B  |
// +----------+----+
// | Music CD | 1  |
// | Book     | 5  |
// | Doll     | 10 |
// +----------+----+
```

## Solution

<details hide>

<summary><h3>Spoiler</h3></summary>

``` python
def draw_table(data: list[dict[str, str | int]], sortBy: str) -> str:
    CORNER = "+"
    HYPHEN = "-"
    VERTICAL_BAR = "|"
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    sorted_data = sorted(data, key=lambda d: d[sortBy])
    max_lengths = {key: max(len(str(d[key])) for d in data) for key in data[0].keys()}

    h_separator = CORNER + CORNER.join(HYPHEN * (max_lengths[key] + 2) for key in max_lengths) + CORNER

    header = VERTICAL_BAR + VERTICAL_BAR.join(
        f" {LETTERS[index]}{' ' * (max_lengths[key] - 1)} " for index, key in enumerate(max_lengths)
    ) + VERTICAL_BAR

    rows = []
    for dictionary in sorted_data:
        row = VERTICAL_BAR + VERTICAL_BAR.join(
            f" {str(dictionary[key])}{' ' * (max_lengths[key] - len(str(dictionary[key])))} " for key in max_lengths
        ) + VERTICAL_BAR
        rows.append(row)

    table = [h_separator, header, h_separator] + rows + [h_separator]
    return "\n".join(table)
```

</details>
