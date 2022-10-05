class InstructionManager:
	def __init__(self, instructionIndex: int, instructions: list):
		self.instruction = instructionIndex
		self.instructions = instructions
	
	def move(self, offset: int):
		if offset >= 0:
			if self.instruction + offset > len(self.instructions)-1:
				return False
			else:
				self.instruction += offset
				return True
		else:
			if self.instruction + offset < 0:
				return False
			else:
				self.instruction += offset
				return True
				
class CellManager:
	def __init__(self, cellIndex: int, cells: int):
		self.cell = cellIndex
		self.cells = [0] * cells
	
	def move(self, offset: int):
		if offset >= 0:
			if self.cell + offset > len(self.cells):
				return False
			else:
				self.cell += offset
				return True
		else:
			if self.cell + offset < 0:
				return False
			else:
				self.cell += offset
				return True
	
	def add(self, number: int):
		self.cells[self.cell] += number

class FunctionManager:
	def __init__(self, cellm: CellManager):
		self.cells = len(cellm.cells)
		self.functions = [[] for _ in range(0, self.cells)]
	
	def add(self, cell: int, instruction: str):
		self.functions[cell].append(instruction)