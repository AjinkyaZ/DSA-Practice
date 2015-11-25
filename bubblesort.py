def bubble_sort(a_list):
	len_a = len(a_list)
	for i in range(len_a-1, 0, -1):
		for j in range(i):
			if(a_list[j]>a_list[j+1]):
				temp = a_list[j]
				a_list[j] = a_list[j+1]
				a_list[j+1] = temp
	return a_list

a = input("enter list of numbers\n")
print "sorted list\n"
print bubble_sort(a)
