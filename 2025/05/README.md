# Challenge 05: ⏱️ The countdown to take off

**Difficulty:** 🟢 Easy
**View:** [adventjs.dev/en/challenges/2025/5](https://adventjs.dev/en/challenges/2025/5)

## Instructions

Elves have a **secret timestamp**: it’s the exact date and time when **Santa Claus takes off with the sleigh** 🛷 to deliver gifts around the world. But at the North Pole they use a super weird format to store the time: `YYYY*MM*DD@HH|mm|ss` NP (example: `2025*12*25@00|00|00 NP`).

Your mission is to write a function that receives:

- `fromTime` → reference date in elf format (`YYYY*MM*DD@HH|mm|ss NP`).
- `takeOffTime` → the same takeoff date, also in elf format.

The function must return:

- The **full seconds** remaining until takeoff.
- If we’re exactly at takeoff time → `0`.
- If takeoff already happened → a **negative number** indicating how many seconds have passed since then.

**🎯 Rules:**

- First convert the elf format to a timestamp. The `NP` suffix indicates official North Pole time (no time zones or DST), so you can treat it as if it were UTC.
- Use differences in **seconds**, not milliseconds.
- Always round down (`floor`): only full seconds.

## 🧩 Examples

```javascript
const takeoff = '2025*12*25@00|00|00 NP'

// from December 24, 2025, 23:59:30, 30 seconds before takeoff
timeUntilTakeOff('2025*12*24@23|59|30 NP', takeoff)
// 30

// exactly at takeoff time
timeUntilTakeOff('2025*12*25@00|00|00 NP', takeoff)
// 0

// 12 seconds after takeoff
timeUntilTakeOff('2025*12*25@00|00|12 NP', takeoff)
// -12
```

## Solution

<details hide>

<summary><h3>Spoiler</h3></summary>

``` python
from datetime import datetime, timezone
import math
      
def time_until_take_off(from_time: str, take_off_time: str) -> int:
    date_format = '%Y*%m*%d@%H|%M|%S NP'
    date_from = datetime.strptime(from_time, date_format)
    date_takeoff = datetime.strptime(take_off_time, date_format)

    delta_seconds = (date_takeoff - date_from).total_seconds()

    return math.floor(delta_seconds)
```

</details>
