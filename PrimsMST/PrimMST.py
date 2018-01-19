def AddPairToGraph(cur_graph, node_pair, edge):
	for idx in range(len(node_pair)):
		cur_node = node_pair[idx]
		other_node = node_pair[1 - idx]
		if cur_node not in cur_graph.keys():
			cur_graph[cur_node] = {other_node: edge}
		else:
			cur_graph[cur_node][other_node] = edge

def ReadInGraph(f_address):
	out_graph = {}
	with open(f_address) as f:
		for line in f:
			splited = [int(each) for each in line.split()]
			if len(splited) == 2: num_node, num_edges = splited[0], splited[1]
			elif len(splited) == 3: 
				connected_nodes = splited[:2]
				edge_cost = splited[2]
				AddPairToGraph(out_graph, connected_nodes, edge_cost)
			else: raise NameError('Wrong Input Length')
	return out_graph, num_node, num_edges

def FindNextNode(cur_MST, cur_graph):
	# initialization 
	if len(cur_MST.keys()) == 0:
		cur_MST = {list(cur_graph.keys())[0]:{}}
	min_cost = float('inf')
	min_nodes = [None, None]
	# for every node in the connect MST
	for each_node in cur_MST:
		cur_costs = cur_graph[each_node]
		for each_next_node in cur_costs:
			if each_next_node not in cur_MST:
				cur_cost = cur_graph[each_node][each_next_node]
				if cur_cost < min_cost: min_cost, min_nodes = cur_cost, [each_node, each_next_node]
	return min_nodes, min_cost


def NaviePrimMST(in_graph):
	'''
	greedy algo to find the MST of a graph 
	find the node with min edge cost to some of the node in the old MST
	'''
	first_node = list(in_graph.keys())[0]
	out_MST = {}
	while len(out_MST.keys()) != len(in_graph.keys()):
		cur_min_nodes, cur_min_cost = FindNextNode(out_MST, in_graph)
		AddPairToGraph(out_MST, cur_min_nodes, cur_min_cost)
	return out_MST

def CalTotalCost(in_MST):
	total = 0
	for each_node in in_MST:
		next_nodes = in_MST[each_node]
		for each_next_node in next_nodes:
			total += next_nodes[each_next_node]
	return total/2

GIVEN_GRAPH, NUM_NODE, NUM_EDGES  = ReadInGraph('edges.txt')
result_MST = NaviePrimMST(GIVEN_GRAPH)
total_cost = CalTotalCost(result_MST)
print(total_cost)