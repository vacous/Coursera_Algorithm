from heapq import *

def FileToList(f_address):
	'''
	from the file address read in txt and output a list of integers
	'''
	with open(f_address) as f:
		content = f.readlines()
	int_list = [int(each) for each in content]
	return int_list
test_list = FileToList('Median.txt')

def HeapMedian(new_val, lower, upper):
	'''
	find the median with two heaps, one min and one max 
	'''
	# initialize 
	if len(lower) == 0: 
		heappush(lower, -new_val)
		return new_val
	# choose one to add
	if new_val > -lower[0]: heappush(upper, new_val)
	else: heappush(lower, -new_val)
	# keep 1/2 invariant 
	if len(lower) - len(upper) == 2:
		heappush(upper, -heappop(lower))
	elif len(upper) - len(lower) == 2:
		heappush(lower, -heappop(upper))
	# print(lower, upper)
	if len(lower) >= len(upper): return -lower[0]
	else: return upper[0] 

def HeapStreamTxt(int_list, lower, upper):
	out_medians = []
	for each in int_list:
		cur_medians = HeapMedian(each, lower, upper)
		out_medians.append(cur_medians)
	return out_medians

lower, upper = [], []
# print(HeapStreamTxt(test_list, lower, upper))
print(sum(HeapStreamTxt(test_list, lower, upper))%10000)