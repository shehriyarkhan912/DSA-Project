class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            print(f"Enqueued {data} to queue")
            return
        self.rear.next = new_node
        self.rear = new_node
        print(f"Enqueued {data} to queue")

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        dequeued_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_node.data

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.front.data

    def display(self):
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.display()  
    print(queue.dequeue())
    print(queue.peek())    
    queue.display()        
