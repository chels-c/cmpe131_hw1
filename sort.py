def sort_list(list):
	n = len(list)
	i = 0
	while i < n:
		k = 0
		while k < (n-i-1):
			if(list[k] > list[k+1]):
				temp = list[k]
				list[k] = list[k+1]			
				list[k+1] = temp
			k+=1
		i+=1
	return list

