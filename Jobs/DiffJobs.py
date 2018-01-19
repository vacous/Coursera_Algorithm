def FileToList(f_address):
	'''
	from the file address read in txt and output a list of integers
	'''
	out_weight_length = []
	with open(f_address) as f:
		for line in f:
			if len(line.split()) == 1:
				task_num = int(line.split()[0])
			else:
				out_weight_length.append([int(each) for each in line.split()])
	return task_num, out_weight_length

task_num, val_list = FileToList('jobs.txt')

class TaskDiff:
	def __init__(self, weight, length):
		self.weight = weight
		self.length = length
	def __str__(self):
		return '(' + str(self.weight) + ', ' + str(self.length) + ') ' + str(self.getDiff())
	def __lt__(self, other_task):
		if self.getDiff() != other_task.getDiff(): 
			return self.getDiff() > other_task.getDiff()
		else:
			return self.getWeight() > other_task.getWeight()
	def getDiff(self): 
		return self.weight - self.length
	def getWeight(self):
		return self.weight
	def getLength(self):
		return self.length

class TaskRatio:
	def __init__(self, weight, length):
		self.weight = weight
		self.length = length
	def __str__(self):
		return '(' + str(self.weight) + ', ' + str(self.length) + ') ' + str(self.getRatio())
	def __lt__(self, other_task):
		return self.getRatio() > other_task.getRatio()
	def getRatio(self): 
		return self.weight*1.0/self.length
	def getWeight(self):
		return self.weight
	def getLength(self):
		return self.length

def CalWeightedCompTime(list_tasks):
	total = 0
	cur_length = 0
	for each_task in list_tasks:
		cur_length += each_task.getLength()
		cur_weight = each_task.getWeight()
		total += cur_weight * cur_length
	return total


task_diff_list = []
task_ratio_list = []
for each_tup in val_list:
 task_diff_list.append(TaskDiff(each_tup[0], each_tup[1]))
 task_ratio_list.append(TaskRatio(each_tup[0], each_tup[1]))
print(CalWeightedCompTime(sorted(task_diff_list)))
print(CalWeightedCompTime(sorted(task_ratio_list)))
