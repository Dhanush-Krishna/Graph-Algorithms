class Node:
    #id
    #adj list

    def __init__(self,i):
        self.id=i
        self.adj_list=[]

    def print_node(self):
        print(self.id,self.adj_list)

    def add_adj(self,n):
        self.adj_list.append(n) #hfhfh

n1=Node(1)
n2=Node(2)
n3=Node(3)

n1.add_adj(n2.id)
n1.add_adj(n3.id)

n1.print_node()


#creating a list of nodes

n=int(input())
node=[]
for i  in range(n):
    nd=Node(i)
    node.append(nd)

for i in range(n):
    node[i].print_node()



