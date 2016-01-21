from collections import defaultdict
import sys
import Queue

vertices = {}

"Define a class for nodes"
class node():

    def __init__(self, id):
        self.id = id
        self.adjacent = {}

    "Function to set the adjacent nodes for vertex in the form of a dictionary"
    def set_adjacent(self,set):
        for item in set:
            if item[0] in vertices.keys():
                new_node = vertices[item[0]]
            else:
                new_node = node(item[0])
                vertices[new_node.id] = new_node

            if new_node not in self.adjacent.keys():
                self.adjacent[new_node] = item[1]


"Function to make nodes for the graph"
def make_node(dict):
    for keys in dict.keys():
        if keys not in vertices.keys():
            curr_node = node(keys)
            vertices[curr_node.id] = curr_node
            curr_node.set_adjacent(dict[curr_node.id])

        else:
            curr_node = vertices[keys]
            curr_node.set_adjacent(dict[curr_node.id])

"Read distance matrix and return a dictionary like {city1:(city2, distance)}"

def readfile(link):
    dict = defaultdict(list)
    file = open(link)
    for lines in file.readlines():
        arr = lines.split()
        # raw_input()
        dict[arr[0].lower()].append((arr[1].lower(), int(arr[2])))
    file.close()
    return dict

"Breadth First search to find the paths from Start to Goal state"
def bfs(vertices, start, goal):
    startN = vertices[start]
    goalN = vertices[goal]
    q = Queue.Queue()
    # path = [startN]
    q.put((startN,[startN],0))

    while not q.empty():
        (vertex,path,dist) = q.get()
        # raw_input()
        # for items in vertex.adjacent.keys():
        #     print items.id
        # for items in path:
        #     print items.id
        for items in list(set(vertex.adjacent.keys()) - set(path)):
            # print items.id
            path1 = path
            if items == goalN:
                print "The path is: ",
                for n in path1+[items]:
                    print n.id,
                print "\nThe distance is: ", dist+vertex.adjacent[items]
                # print path1+[items],dist+vertex.adjacent[items]
            else:
                # raw_input()
                # path1.append(items)
                # print "item",items.id
                # print "path",
                # for items in path1:
                #     print items.id,
                # print "dist", dist+vertex.adjacent[items]
                q.put((items,path1+[items],dist+vertex.adjacent[items]))


if __name__ == "__main__":
    ar = readfile("distance_matrix.txt")
    print ar
    make_node(ar)
    # print "Enter Start and the Goal cities"
    bfs(vertices,"arad", "bucharest")
    # for k in vertices.keys():
    #     # print k
    #     print vertices[k].id
    #     for items in vertices[k].adjacent.keys():
    #         raw_input()
    #         print items.id, vertices[k].adjacent[items]
    # arad = vertices["Arad"]
    # for items in arad.adjacent.keys():
    #     print items.id,arad.adjacent[items]


