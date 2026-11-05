import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	rows,cols = new_shape
	flat = [value for row in a for value in row]
	if rows < 0 or cols < 0 or rows*cols != len(flat):
		return []
	reshaped_matrix = [flat[i*cols:(i+1)*cols] for i in range(rows)]
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	return reshaped_matrix