class Node:  
    def __init__(self, data):  
        self.data = data  
        self.next = None  
  
class SinglyLinkedList:  
    def __init__(self):  
        self.head = None  
  
    def create(self, n):  
        for i in range(n):  
            data = int(input(f"Enter the data of node {i + 1}: "))  
            new_node = Node(data)  
            if not self.head:  
                self.head = new_node  
                current = self.head  
            else:  
                current.next = new_node  
                current = new_node  
  
    def display(self):  
        temp = self.head  
        if not temp:  
            print("List is EMPTY")  
        while temp:  
            print(f"DATA IS -> {temp.data}")  
            temp = temp.next  
  
    def count(self):  
        temp = self.head  
        count = 0  
        while temp:  
            count += 1  
            temp = temp.next  
        return count  
  
    def sum(self):  
        temp = self.head  
        total = 0  
        while temp:  
            total += temp.data  
            temp = temp.next  
        return total  
  
    def insert_pos(self, data):  
        pos = int(input("Enter position to insert: "))  
        new_node = Node(data)  
  
        if pos == 1:  
            new_node.next = self.head  
            self.head = new_node  
        else:  
            temp = self.head  
            for i in range(pos - 2):  
                if not temp:  
                    print("Invalid position")  
                    return  
                temp = temp.next  
            new_node.next = temp.next  
            temp.next = new_node  
  
    def search(self, key):  
        temp = self.head  
        index = 0  
        while temp:  
            if temp.data == key:  
                return index  
            index += 1  
            temp = temp.next  
        return -1  
  
    def delete_ra(self):  
        pos = int(input("Enter position to delete: "))  
        if pos == 1:  
            deleted_node = self.head  
            self.head = self.head.next  
            del deleted_node  
        else:  
            temp = self.head  
            for i in range(pos - 2):  
                if not temp:  
                    print("Invalid position")  
                    return  
                temp = temp.next  
            if not temp or not temp.next:  
                print("Invalid position")  
                return  
            deleted_node = temp.next  
            temp.next = temp.next.next  
            del deleted_node  
  
    def delSLL(self):  
        temp = self.head  
        while temp:  
            deleted_node = temp  
            temp = temp.next  
            del deleted_node  
        self.head = None  
        print("Successfully deleted all nodes")  
  
    def chsorte(self):  
        temp = self.head  
        x = -32768  
        while temp:  
            if temp.data < x:  
                return False  
            x = temp.data  
            temp = temp.next  
        return True  
  
    def dupl(self):  
        current = self.head  
        while current:  
            index = current  
            while index.next:  
                if current.data == index.next.data:  
                    deleted_node = index.next  
                    index.next = index.next.next  
                    del deleted_node  
                else:  
                    index = index.next  
            current = current.next  
        print("Duplicates successfully removed")  
  
    def Asortt(self):  
        p = self.head  
        while p.next:  
            q = p.next  
            while q:  
                if p.data > q.data:  
                    p.data, q.data = q.data, p.data  
                q = q.next  
            p = p.next  
  
    def revr(self):  
        p = self.head  
        A = []  
        while p:  
            A.append(p.data)  
            p = p.next  
        p = self.head  
        i = len(A) - 1  
        while p:  
            p.data = A[i]  
            i -= 1  
            p = p.next  
  
    def getnode(self, index):  
        current = self.head  
        length = 0  
        while current:  
            if length == index:  
                return current.data  
            length += 1  
            current = current.next  
        return -1  
  
    def detectandremov(self):  
        slow = self.head  
        fast = self.head  
        prev = None  
  
        while slow and fast and fast.next:  
            prev = slow  
            slow = slow.next  
            fast = fast.next.next  
  
            if slow == fast:  
                self.removeloop(prev)  
                print("Cycle detected and removed.")  
                return True  
  
        print("No cycle detected.")  
        return False  
  
    def removeloop(self, prev):  
        start = self.head  
        loop = prev.next  
  
        while start != loop:  
            start = start.next  
            prev = loop  
            loop = loop.next  
  
        prev.next = None  
  
    def getend(self, pos):  
        length = 0  
        p = self.head  
        while p:  
            p = p.next  
            length += 1  
  
        if length < pos:  
            print("Out of range")  
            return  
  
        p = self.head  
        for i in range(1, length - pos + 1):  
            p = p.next  
  
        print(f"{p.data} is the data")  
  
    def occurence(self, sf):  
        p = self.head  
        count = 0  
        while p:  
            if p.data == sf:  
                count += 1  
            p = p.next  
        return count  
  
    def swapNodes(self, x, y):  
        if x == y:  
            return  
  
        prevX = None  
        currX = self.head  
        while currX and currX.data != x:  
            prevX = currX  
            currX = currX.next  
  
        prevY = None  
        currY = self.head  
        while currY and currY.data != y:  
            prevY = currY  
            currY = currY.next  
  
        if not currX or not currY:  
            return  
  
        if prevX:  
            prevX.next = currY  
        else:  
            self.head = currY  
  
        if prevY:  
            prevY.next = currX  
        else:  
            self.head = currX  
  
        currX.next, currY.next = currY.next, currX.next  
  
    def pairwiseswap(self):  
        current = self.head  
        while current and current.next:  
            current.data, current.next.data = current.next.data, current.data  
            current = current.next.next  
  
  
# Main program  
if __name__ == "__main__":  
    linked_list = SinglyLinkedList()  
    while True:  
        print("\n1. Create\n2. Display\n3. Count\n4. Sum of all nodes\n5. Anywhere insert")  
        print("6. Search an element\n7. Delete option\n8. Check Sort\n9. Remove duplicate\n10. To Reverse ")  
        print("11. Get node data\n12. Check for cycle detection\n13. Get node from end\n14. Occurrence of data")  
        print("15. Swap nodes in a linked list\n16. Pairwise swap\n17. Exit")  
        choice = int(input("Enter your choice: "))  
  
        if choice == 1:  
            n = int(input("Enter number of nodes: "))  
            linked_list.create(n)  
        elif choice == 2:  
            print("The nodes are:")  
            linked_list.display()  
        elif choice == 3:  
            t = linked_list.count()  
            print(f"The length of the linked list: {t}")  
        elif choice == 4:  
            s = linked_list.sum()  
            print(f"The sum of all elements in the linked list is: {s}")  
        elif choice == 5:  
            data = int(input("Enter the item to be inserted: "))  
            linked_list.insert_pos(data)  
        elif choice == 6:  
            keyse = int(input("Enter element to search: "))  
            index = linked_list.search(keyse)  
            if index >= 0:  
                print(f"{keyse} found at position {index + 1}")  
            else:  
                print("Not found")  
        elif choice == 7:  
            print("1. Delete a node\n2. Delete the linked list")  
            chh = int(input("Enter your choice: "))  
            if chh == 1:  
                linked_list.delete_ra()  
            else:  
                linked_list.delSLL()  
        elif choice == 8:  
            if linked_list.chsorte():  
                print("The list is sorted.")  
            else:  
                print("The list is not sorted.")  
                ask = input("Do you want to sort the list (y/n): ")  
                if ask == 'y':  
                    linked_list.Asortt()  
                    linked_list.display()  
        elif choice == 9:  
            linked_list.dupl()  
        elif choice == 10:  
            linked_list.revr()  
            linked_list.display()  
        elif choice == 11:  
            index = int(input("Enter position of node to get Data: "))  
            data = linked_list.getnode(index - 1)  
            if data != -1:  
                print(f"Nth Node data of LinkedList is: {data}")  
        elif choice == 12:  
            linked_list.detectandremov()  
        elif choice == 13:  
            pos = int(input("Enter a position to get a value: "))  
            data = linked_list.getend(pos)  
        elif choice == 14:  
            sf = int(input("Enter the data to see its frequency: "))  
            count = linked_list.occurence(sf)  
            print(f"Count of {sf} is {count}")  
        elif choice == 15:  
            x, y = map(int, input("Enter the numbers to be swapped: ").split())  
            print("Before swapping:")  
            linked_list.display()  
            linked_list.swapNodes(x, y)  
            print("After swapping:")  
            linked_list.display()  
        elif choice == 16:  
            print("Before swapping:")  
            linked_list.display()  
            print("After pairwise swapping:")  
            linked_list.pairwiseswap()  
            linked_list.display()  
        elif choice == 17:  
            print("Exiting program.")  
            break  
        else:  
            print("INVALID CHOICE")  
