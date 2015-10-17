def bubble_sort(a_list):
	len_a = len(a_list)
	for p_num in range(len_a - 1, 0, -1):
		for i in range(p_num):
			temp = a_list[i]
			a_list[i] = a_list[i+1]
			a_list[i+1] = temp
	return a_list

a = input("enter list of numbers\n")
print "sorted list\n"
print bubble_sort(a)