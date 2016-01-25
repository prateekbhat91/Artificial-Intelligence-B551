"""Search Methods to find the paths form source to destination"""

"@@authors = Prateek Bhat and Sanjana Agarwal"

from collections import defaultdict
import sys
import Queue
import re

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
    try:
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

                    print "\nThe distance is: ",dist+vertex.adjacent[items]
                    return
                else:
                    q.put((items,path+[items],dist+vertex.adjacent[items]))
        # print "No path found"
    except:
        print "Node not found"


"Depth First Search"

def dfs(vertices, start, goal):
    try:
        startN = vertices[start]
        goalN = vertices[goal]
        stack=[]
        stack.append((startN,[startN],0))

        while stack:
            (vertex,path,dist) = stack.pop()
            for items in list(set(vertex.adjacent.keys())-set(path)):
                if items == goalN:
                    print "The path is: ",
                    for n in path+[items]:
                        print n.id,",",

                    print "\nThe distance is: ",dist+vertex.adjacent[items]
                    return
                else:
                    stack.append((items,path+[items],dist+vertex.adjacent[items]))
    except:
        print "Node not found"

if __name__ == "__main__":
    ar = readfile("distance_matrix.txt")
    make_node(ar)

    print "Enter the input as comma separated."
    print "\nFor example city1,city2,algo name(BFS, DFS, IDE)"
    print "\nPrint \"exit\" to Exit the program"
    while (1):
        print "\nEnter new input."
        tempstr = raw_input().lower()
        pattern = re.compile("^\s+|\s*,\s*|\s+$")               #Find pattern of spaces before and after comma
        temparr = [x for x in pattern.split(tempstr) if x]      #Remove spaces beofre a node name

        if temparr[0] == "exit":                                #Check for exit condition
                exit()

        elif len(temparr) == 3:                                 #check if input is in right format
                if temparr[2].lower() == "bfs":
                    bfs(vertices, temparr[0], temparr[1])
                    print "\n"

                elif temparr[2].lower() == "dfs":
                    dfs(vertices, temparr[0], temparr[1])
                    print "\n"

                elif temparr[2].lower() == "ide":
                    # ideep(vertices, temparr[0], temparr[1])
                    pass

                else:
                    print "Enter the Algo name as BFS, DFS, IDE. "
        else:
            print "Enter input in format \"City1,City2,Algo name(BFS, DFS, IDE)\". "
