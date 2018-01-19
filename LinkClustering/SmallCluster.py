def ReadInGraph(f_adderss):
	out_graph = []
	appeared_nodes = set()
	with open(f_adderss) as file:
		for line in file:
			splited = [int(val) for val in line.split()]
			if len(splited) == 1: num_nodes = splited
			else: 
				appeared_nodes.add(splited[0])
				appeared_nodes.add(splited[1])
				out_graph.append((splited[2], (min(splited[:2]), max(splited[:2]))))
	return out_graph, appeared_nodes

class Cluster:
	def __init__(self, ini_node):
		self.connected = {ini_node:{}}
	def __str__(self):
		return str(self.connected)

	def mergeTwoClusters(self, c_1, c_2):
		''' merge c_1 into c_2 '''
		for each_node in c_1.connected:
			each_edges = c_1.connected[each_node]
			if each_node not in c_2.connected:
				c_2.connected[each_node] = each_edges
			else:
				for each_other_node in each_edges:
					c_2.connected[each_node][each_other_node] = each_edges[each_other_node]

	def addNewEdge(self, old_cluster, new_edge):
		edge_len = new_edge[0]
		node_pair = new_edge[1]
		for idx in range(len(node_pair)):
			other_idx = abs(idx - 1)
			this_node, other_node = node_pair[idx], node_pair[other_idx]
			if this_node not in old_cluster.connected:
				old_cluster.connected[this_node] = {other_node: edge_len}
			else:
				old_cluster.connected[this_node][other_node] = edge_len
		
	def merge(self, other_cluster, new_edge):
		''' compare the cluster size, merge the smaller one into the larger one '''
		self.mergeTwoClusters(other_cluster, self)
		self.addNewEdge(self, new_edge)

	def getNodeNum(self): return len(self.connected)

def RedirectPointers(in_nodes, old_cluster, new_cluster_idx):
	old_nodes = old_cluster.connected.keys()
	for each_n in old_nodes:
		in_nodes[each_n-1] = new_cluster_idx

def SingleLinkCluster(in_nodes, in_graph, cluster_limit):
	if len(in_nodes) < cluster_limit: 
		print('Impossible to cluster to the given limit: alreay very few')
		return -1
	elif len(in_nodes) == cluster_limit:
		print('No clustering required: limit satisfied')
	else:
		out_cluster = {}
		for each_node in in_nodes:
			out_cluster[each_node] = Cluster(each_node)
		for each_edge in in_graph:
			n_1, n_2 = each_edge[1][0] - 1, each_edge[1][1] - 1 
			c_idx_1, c_idx_2 = in_nodes[n_1], in_nodes[n_2]
			if c_idx_1 != c_idx_2: # check if already in the same cluster
				c_1, c_2 = out_cluster[c_idx_1], out_cluster[c_idx_2]
				if c_1.getNodeNum() >= c_2.getNodeNum(): 
					c_1.merge(c_2, each_edge)
					RedirectPointers(in_nodes, c_2, c_idx_1)
					out_cluster.pop(c_idx_2)
				else:
					c_2.merge(c_1, each_edge)
					RedirectPointers(in_nodes, c_1, c_idx_2)
					out_cluster.pop(c_idx_1)
			if len(out_cluster) == cluster_limit-1: 
				return each_edge[0]
	print('No Spacing for the given limit')
	return in_graph[-1][0]

GIVEN_GRAPH, ALL_VALS = ReadInGraph('clustering1.txt')
GIVEN_GRAPH = sorted(GIVEN_GRAPH)
ALL_NODES = [cluster_idx for cluster_idx in ALL_VALS]
# print(GIVEN_GRAPH)

# test
# test_g = [[(1,(1,2)), (2,(3,4)), (3,(2,4)), (4,(1,3))], 
# 		  [(1,(1,3)),(2,(1,6)),(3,(2,3)),(4,(1,2)),(4,(1,4)),(5,(1,5)),(6,(6,7))]]
# test_n = [[each for each in range(1,5)], [each for each in range(1,8)]]

print(SingleLinkCluster(ALL_NODES, GIVEN_GRAPH, 4))










		





