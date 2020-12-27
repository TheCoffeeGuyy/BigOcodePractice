input = input()
stack = []
for symbol in input:
  if symbol == 'C':
    stack.append(12)
  elif symbol == 'O':
    stack.append(16)
  elif symbol == 'H':
    stack.append(1)
  elif symbol == '(':
    stack.append('(')
  elif symbol == ')':
    mass = 0
    while stack[-1] != '(':
      mass += stack.pop()
    stack.pop()
    stack.append(mass)
  elif symbol.isdigit():
    intVal = int(symbol) * stack.pop()
    stack.append(intVal)
print(sum(stack))