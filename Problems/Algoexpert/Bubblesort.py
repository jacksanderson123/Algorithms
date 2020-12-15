def bubbleSort(array):

	for i in range(len(array)):
		no_swaps = True
		for j in range(len(array)- 1):
			if array[j] > array[j + 1]:
				array[j], array[j+1] = array[1+j], array[j]
				no_swaps = False
		if no_swaps:
			break
	return array

if __name__ == "__main__":
    array = [8, 5, 2, 9, 5, 6, 3]
    bubbleSort(array)