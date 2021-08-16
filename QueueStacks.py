class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self, x):
        #Insert element last
        self.s1.append(x)
        print(self.s1)

    def deQueue(self):

        #Check if the queue is already empty
        if len(self.s1) == 0:
            print("Q is Empty")
            return ""

        while len(self.s1) != 1:
            #Move the last element from s1 to s2
            self.s2.append(self.s1[-1])
            self.s1.pop()

        #Check if we have already reached first element and take it out
        if len(self.s1) == 1:
            x = self.s1[-1]
            self.s1.pop()

        while len(self.s2) != 0:
            #Move back the previous element back to s1
            self.s1.append(self.s2[-1])
            #Clear s2 for next use
            self.s2.pop()

        #Return the queue and value taken out
        print("Queue: ", self.s1)
        return x
                
# Driver code
if __name__ == '__main__':
    q = Queue()
    
    print("Queue:")
    q.enQueue(3)
    q.enQueue(2)
    q.enQueue(1)

    print("DeQueue:")
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())


        
        
