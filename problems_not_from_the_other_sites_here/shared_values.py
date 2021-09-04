def get_shared_values_in_place(list1: list, list2: list):
	i = 0
	j = 0

	while i < len(list1) and j < len(list2):
		cur1 = list1[i]
		cur2 = list2[j]

		if cur1 == cur2:
			i+=1
			j+=1
		elif cur1 < cur2:
			j+=1
		else: # cur1 > cur2
			list1.pop(i)

		if j >= len(list2):
			ret_list = list1[0:(i-1)]

	return ret_list

def get_shared_values(list1: list, list2: list):
	dict1 = {}

	for elem in list1:
		dict1[elem] = 0

	for elem in list2:
		if elem in dict1:
			dict1[elem] = 1

	for elem in dict1:
		if dict1[elem] == 0:
			dict1.pop(elem)

	return list(dict1.keys())

def get_shared_values_concise(list1: list, list2: list):
	return [x for x in list1 if x in set(list2)]


	# return set(list1).intersection(set(list2))