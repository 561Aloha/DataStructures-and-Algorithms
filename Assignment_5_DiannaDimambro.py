#Queue that we manipulate
#Verison 2 Stacks
"""Dianna Dimambro, April 14th,2023
Assignment 5. Professor Taebi"""

class ArrayStack:

  def __init__ (self, maxlen = 5):
    self._data = [ ] # nonpublic list instance
    self.maxlen = maxlen
  
  def __len__ (self):
    return len(self._data)

  def is_empty(self):
    return len(self._data) == 0
  
  def push(self, e):
    try:
      if len(self._data) == self.maxlen:
        raise Exception("Error: Stack is full")
      else:
        self._data.append(e) # new item stored at end of list
    except Exception as ex:
      print(ex)
  
  def top(self):
    if self.is_empty( ):
      raise Empty( 'Stack is empty' )
    return self._data[-1] # the last item in the list
    
  def pop(self):
    if self.is_empty( ):
      raise Empty( 'Stack is empty' )
    return self._data.pop( ) # remove last item from list
  
  def peek(self):
    if self.is_empty():
      raise Empty('Stack is Empty')
    return self._data[-1]
  

  def print_elements(self):
    result = "Stack elements: "
    for item in self._data:
        result += str(item) + " "
    return result

  def pop_pop(self):
      if len(self._data) == 0:
          return "It's been completed"
      else:
          self._data.pop()
          return self.pop_pop()                   #what makes this a recursive function



class StackFullError():
  pass

class Empty(Exception): 
  pass


def reverse_file(filename):
  print("reversefile executing")
  S = ArrayStack()
  original = open(filename)
  for line in original:
    for i in line:
      S.push(i) # we will re-insert newlines when writing
  original.close( )
  # now we overwrite with contents in LIFO order
  output = open(filename, 'w' ) # reopening file overwrites original
  while not S.is_empty( ):
    output.write(S.pop( )) # re-insert newline characters
  output.close( )


if __name__ == "__main__":
  S = ArrayStack( )               # contents: [ ]
  S.push(5)                       # contents: [5]
  S.push(3)                       # contents: [5, 3]
  print(len(S))                   # contents: [5, 3]; outputs 2
  print(S.pop( ))                 # contents: [5]; outputs 3
  print(S.is_empty())             # contents: [5]; outputs False
  print(S.pop( ))                 # contents: [ ]; outputs 5
  print(S.is_empty())             # contents: [ ]; outputs True
  S.push(7)                       # contents: [7]
  S.pop()
  S.push(9)                       # contents: [7, 9]
  print(S.top( ))                 # contents: [7, 9]; outputs 9
  S.push(4)                       # contents: [7, 9, 4]
  print(len(S))                   # contents: [7, 9, 4]; outputs 3
  print(S.pop( ))                 # contents: [7, 9]; outputs 4
  S.push(6)                       # contents: [7, 9, 6]
  S.pop()
  S.pop()                         #trying to empty the queue


  print()
  print('The offical error when I push past the 5 limited stack: ')
  S.push(1)
  S.push(2)                       # contents: [5]
  S.push(3) 
  S.push(4)                       # contents: [5]
  S.push(5) 
  S.push(6)             

  print()
  print('New Stack: ')
  print('The Length of the New Stack: ',len(S))
  print('The Top Element of the stack: ',(S.peek()))  
  
  print()
  print(S.pop_pop())

  print("The length of the stack is now", len(S))
  print ("-------------------------------------------------------------------")
  print ()
  print("Problem 3: ")





class Queue(object):
  def __init__(self, size):                   # Constructor
    self.__maxSize = size                     # Size of [circular] array
    self.__que = [None] * size                # Queue stored as a list
    self.__front = 1                          # Empty Queue has front 1
    self.__rear = 0                           # after rear and
    self.__nItems = 0                         # No items in queue
  
  def enqueue(self, item):                    # Insert item at rear of queue
    if self.is_full():                        # if not full
      raise Exception("Queue overflow")
    self.__rear += 1                          # Rear moves one to the right
    if self.__rear == self.__maxSize:         # Wrap around circular array
      self.__rear = 0
    self.__que[self.__rear] = item            # Store item at rear
    self.__nItems += 1
    return True

  def dequeue(self):                          # Remove front item of queue
    if self.is_empty():                       # and return it, if not empty
      raise Exception("Queue underflow")
    front = self.__que[self.__front]          # get the value at front
    self.__que[self.__front] = None           # Remove item reference
    self.__front += 1                         # front moves one to the right
    if self.__front == self.__maxSize:        #  Wrap around circular array
      self.__front = 0
    self.__nItems -= 1
    return front
  
  def first(self):                          # Return frontmost item
    return None if self.is_empty() else self.__que[self.__front]
  
  def is_empty(self): 
    return self.__nItems == 0
  
  def is_full(self): 
    return self.__nItems == self.__maxSize
  
  def __len__(self): 
    return self.__nItems
  
  def __str__(self):                        # Convert queue to string
    ans = "["                               # Start with left bracket
    for i in range(self.__nItems):          # Loop through current items
      if len(ans) > 1:                        # Except next to left bracket,
        ans += ", "                             # separate items with comma
      j = i + self.__front                    # Offset from front
      if j >= self.__maxSize:                 # Wrap around circular array
        j -= self.__maxSize
      ans += str(self.__que[j])               # Add string form of item
    ans += "]"                              # Close with right bracket
    return ans


if __name__ == "__main__":
  Q= Queue(20)                              #create an object of array queue
  Q.enqueue(5)
  Q.dequeue()
  print('True or False, Is the Queue Empty?: ')
  print(Q.is_empty())
  print('The Length is: ',len(Q))

  print()
  Q.enqueue(5)            # outputs [5]
  Q.enqueue(3)            # outputs [5,3]
  Q.dequeue()             # outputs [5] takes out three
  Q.enqueue(2)            # outputs [5,2] 
  Q.enqueue(8)            # outputs [5,2,8] 
  Q.dequeue()             # outputs [5,2] takes out 8
  Q.dequeue()             # outputs [5] takes out 2
  Q.enqueue(9)            # outputs [5,2,9] 
  Q.enqueue(1)            # outputs [5,2,9,1] 
  Q.dequeue()             # outputs [5,2,9]  takes out 1
  Q.enqueue(7)            # outputs [5,2,9,7] 
  Q.enqueue(6)            # outputs [5,2,9,7,6] 
  Q.dequeue()             # outputs [5,2,9,7]  takes out 6
  Q.dequeue()             # outputs [5,2,9] takes out 7
  Q.enqueue(4)            # outputs [5,2,9,7,4] 
  Q.dequeue()             # outputs [5,2,9,7] takes out 4
  print()
  print('Is the Queue Empty?: ',Q.is_empty() )
  print('Whats the top of the queue: ', Q.first())
  print('Is this full?: ',Q.is_full())
  print('The Length is: ',len(Q))
  print('Print Elements: ', str(Q))
  Q.dequeue()
  Q.dequeue()

  print('The Length is: ',len(Q))

""" Question 4
32 enqueues - the 15 dequeues + the 5 of which raised Empty errors that were ignored
32 - 15 + 5 = 22

Therefore, the current size of Q is 22.

"""
