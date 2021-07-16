a = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
i = 0
max = 0
len_max = 0
min = a[0]
len_min = 0
while i < len(a):
	if len_max < len(a[i]):
		len_max = len(a[i])
		max = a[i]
	if len_min > len(a[i]):
		min = a[i]
		len_min = len(a[i])
	i += 1
print(len_max,max)
print(len_min,min)

# find max and min in nested list and print len also 