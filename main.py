import managers
import errors

cells = managers.CellManager(0, 65535)
instructions = managers.InstructionManager(0, [
'cells.add(1)',
'cells.add(-1)',
'if not cells.move(cells.cells[cells.cell]):\n    print(f"{index + 1}:CellError: {errors.Errors.CellError[1]}")\n    exit(-1)',
'points[0] = cells.cell',
'points[1] = cells.cell',
'cells.cells[cells.cell] = points[0] + points[1]',
'cells.cells[cells.cell] = points[0] - points[1]',
'cells.cells[cells.cell] = cells.cells[cells.cell]*-1',
'cells.cells[points[1]] = cells.cells[points[0]]'
])
functions = managers.FunctionManager(cells)
flags = [0, 0, 0, 0, 0, 0, 0, 0]
points = [0, 0]

def interpret(code):
	for index, char in enumerate(code):
		if flags[1]:
			if char == ")":
				flags[1] = 0
			
			else:
				functions.add(cells.cell, char)
		else:
			if char == "#":
				interpret(functions.functions[cells.cell])
				
			if char == '=':
				flags[0] = 1
			
			if char == ':':
				exec(instructions.instructions[instructions.instruction])
					
			
			if char == '>':
				if flags[0]:
					if not instructions.move(1):
						print(f'{index + 1}:InstructionError: {errors.Errors.InstructionError[1]}')
						exit(-1)
					flags[0] = 0
				else:	
					if not cells.move(1):
						print(f'{index + 1}:CellError: {errors.Errors.CellError[1]}')
						exit(-1)
					
			if char == '<':
				if flags[0]:
					if not instructions.move(-1):
						print(f'{index + 1}:InstructionError: {errors.Errors.InstructionError[1]}')
						exit(-1)
					flags[0] = 0
				else:
					if not cells.move(-1):
						print(f'{index + 1}:CellError: {errors.Errors.CellError[1]}')
						exit(-1)
			
			if char == "(":
				flags[1] = 1

# 0 instruction = + 1 to cell
# 1 instruction = - 1 to cell
# 2 instruction = move cell to value of cell
# 3 instruction = point 1
# 4 instruction = point 2
# 5 instruction = set value of current cell point 1 + point 2
# 6 instruction = set value of current cell point 1 - point 2
# 7 instruction = invert value
# 8 instruction = clone point 1 to point 2
code = ''
interpret(code) # interpret code
#print(functions.functions[0:10])
#print({"cell": {cells.cell: cells.cells[cells.cell]}, "inst": {instructions.instruction: instructions.instructions[instructions.instruction]}})