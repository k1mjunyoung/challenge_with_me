
# 원형 연결 리스트를 객체지향적으로 구현 
class Node: 
    def __init__(self,data): 
        self.data  = data 
        self.next = None 
class Circular_LinkedList : 
    def __init(self): 
        self.head = None 

# 마지막 노드에 오른쪽에 새로운 노드를 추가하는 코드 
# 마지막 노드의 다음 노드가 첫 노드가 되어야함 
        
def append(self,data):
    if self.head is None: 
        self.head=None(data) 
        node = self.head 

        #다음 노드는 자기 자신 참조 
        node.next = self.head 

    else: 
        node = self.head 
        while node.next != self.head:
            node =node.next 

        new_node = Node(data)
        node.next = new_node
        new_node.next = self.head 
        
