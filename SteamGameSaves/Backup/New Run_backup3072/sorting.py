
def quicksort_tuples(items):
	if len(items) <= 1:
		return items

	pivot = items[len(items) // 2][0]
	
	left = []    # Plus grands que le pivot
	middle = []  # Égaux au pivot
	right = []   # Plus petits que le pivot
	
	for item in items:
		value = item[0]
		if value > pivot:
			left.append(item)
		elif value == pivot:
			middle.append(item)
		else:
			right.append(item)
	
	return quicksort_tuples(left) + middle + quicksort_tuples(right)


def selection_sort_tuples(items):
	n = len(items)
	
	for i in range(n):
		# Trouver l'index du maximum dans le reste de la liste
		max_index = i
		for j in range(i + 1, n):
			if items[j][0] > items[max_index][0]:
				max_index = j
		
		# Échanger avec la position actuelle
		temp = items[i]
		items[i] = items[max_index]
		items[max_index] = temp
	
	return items