'''
Challenge #25: 🪄 Execute the magical language

We have already distributed all the gifts! Back at the workshop, preparations for next year are already beginning.

A genius elf is creating a magical programming language 🪄 that will help streamline the delivery of gifts to children in 2025.

Programs always start with the value 0, and the language is a string where each character represents an instruction:

> Moves to the next instruction
+ Increments the current value by 1
- Decrements the current value by 1
[ and ]: Loop. If the current value is 0, jump to the instruction after ]. If it is not 0, go back to the instruction after [
{ and }: Conditional. If the current value is 0, jump to the instruction after }. If it is not 0, continue to the instruction after {
You need to return the value of the program after executing all the instructions.

execute('+++') // 3
execute('+--') // -1
execute('>+++[-]') // 0
execute('>>>+{++}') // 3
execute('+{[-]+}+') // 2
execute('{+}{+}{+}') // 0
execute('------[+]++') // 2
execute('-[++{-}]+{++++}') // 5

Note: A conditional can have a loop inside, and a loop can also have a conditional inside. But two loops or two conditionals are never nested.
'''

def execute_original(code: str) -> int:
  value = 0
  index = 0

  loop_init = 0
  loop_end = 0

  code_length = len(code)

  while index < code_length:
    instruction = code[index]
    match instruction:
      case ">":
        index += 1
      case "+":
        value += 1
        index += 1
      case "-":
        value -=1
        index += 1
      case "[":
        loop_init = index + 1
        loop_end = code.find("]", index) + 1
        index = loop_end if value == 0 else loop_init
      case "]":
        index = loop_end if value == 0 else loop_init
      case "{":
        conditional_init = index + 1
        conditional_end = code.find("}", index) + 1
        index = conditional_end if value == 0 else conditional_init
      case "}":
        index += 1

  return value

def execute(code: str) -> int:
    value = 0
    index = 0

    # Precompute matching brackets for "["/"]" and "{" / "}"
    bracket_map = {}
    stack = []

    for i, instruction in enumerate(code):
        if instruction in "[{":
            stack.append((instruction, i))
        elif instruction in "]}":
            _, position = stack.pop()
            bracket_map[position] = i
            bracket_map[i] = position

    while index < len(code):
        instruction = code[index]

        match instruction:
            case ">":
                index += 1
            case "+":
                value += 1
                index += 1
            case "-":
                value -= 1
                index += 1
            case "[":
                if value == 0:
                    index = bracket_map[index] + 1
                else:
                    index += 1
            case "]":
                if value != 0:
                    index = bracket_map[index]
                else:
                    index += 1
            case "{":
                if value == 0:
                    index = bracket_map[index] + 1
                else:
                    index += 1
            case "}":
                index += 1

    return value
  
  # Main program
print(execute('+++'))
print(execute('+--'))
print(execute('>+++[-]'))
print(execute('>>>+{++}'))
print(execute('+{[-]+}+'))
print(execute('{+}{+}{+}'))
print(execute('------[+]++'))
print(execute('-[++{-}]+{++++}'))