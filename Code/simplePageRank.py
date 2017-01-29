import networkx as nx
import csv

G = nx.Graph()

file = open('weights_to_stations.csv', 'rb')
reader = csv.reader(file,skipinitialspace=True,quotechar="'",delimiter=',')

StationWeight = {}

flag = True
for x in reader:
	if flag:
		flag = not flag
	else:
		StationWeight[x[0]] = int(x[2])
		G.add_node(x[0])

file.close()
pageRank  = nx.pagerank(G,personalization=StationWeight)

pr_list = []

for x in pageRank:
	pr_list.append([x, pageRank[x]])

outputfile = open("pageRankSimple.csv", 'wb')
wr = csv.writer(outputfile, quoting=csv.QUOTE_NONE,delimiter=',')
wr.writerows(pr_list)