import time

def FileToList(f_address):
	'''
	from the file address read in txt and output a list of integers
	'''
	with open(f_address) as f:
		content = f.readlines()
	int_list = [int(each) for each in content]
	return int_list

hashed_test_list = set(FileToList('IntList.txt'))

print(len(hashed_test_list))

def HasDistinctPair(total_val, hashed_int_list):
	'''
	add ints from the list into a hash set and 
	find the Sum - cur_val for each cur_val 
	'''
	for each_val in hashed_int_list:
		diff = total_val - each_val
		if diff != each_val and diff in hashed_int_list: 
			return True
	return False

def NumDistinctPairInRange(value_range, hashed_int_list):
	'''
	find the number of target value within the value range that 
	in the hashed list there are distinct pair x+y = target value 
	'''
	total_num = 0
	count = 0
	init_time = time.time()
	for each_target in value_range:
		count += 1
		print(count)
		if HasDistinctPair(each_target, hashed_int_list):
			total_num += 1
		print(time.time() - init_time)
	print('--------------------------------------')
	return total_num
print('--------------------------------------')
print(NumDistinctPairInRange(range(-10000,10001), hashed_test_list))