"""Search Methods to find the paths form source to destination"""

"@@authors = Prateek Bhat and Sanjana Agarwal"

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

"Breadth First search"
def bfs(vertices, start, goal):
    startN = vertices[start]
    goalN = vertices[goal]
    q = Queue.Queue()
    q.put((startN,[startN],0))

    while not q.empty():
        (vertex,path,dist) = q.get()
        # for items in path:
        #     print items.id
        for items in list(set(vertex.adjacent.keys()) - set(path)):
            if items == goalN:
                print "The path is: ",
                for n in path+[items]:
                    print n.id,",",

                print "\nThe distance is: ", dist+vertex.adjacent[items]
                pass
            else:
                q.put((items,path+[items],dist+vertex.adjacent[items]))


if __name__ == "__main__":
    ar = readfile("distance_matrix.txt")
    # print ar
    make_node(ar)
    bfs(vertices,"arad", "bucharest")

    # for items in arad.adjacent.keys():
    #     print items.id,arad.adjacent[items]



