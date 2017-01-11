def bubble_sort(a_list):
	len_a = len(a_list)
	for i in range(len_a-1, 0, -1):
		for j in range(i):
			if(a_list[j]>a_list[j+1]):
				temp = a_list[j]
				a_list[j] = a_list[j+1]
				a_list[j+1] = temp
	return a_list


def main():
    a = raw_input("enter array\n").split(' ')
    a = [int(n) for n in a]
    print "original array :\n", a
    print "sorted array :\n", bubble_sort(a)


if __name__ == "__main__":
    main()
