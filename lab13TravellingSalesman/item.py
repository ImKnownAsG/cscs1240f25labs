class Item:
    _object = None
    _next = None
    _prev = None
    _iter = None
    
    def __init__(self, obj = None): 
        #called anytime a new instance of Item is created
        #sets a default value of None to _object if nothing 
        #is provided in the call
        self._object = obj
    
    def object(self):
        #helper function to read value - write is obscured 
        #behind '_method' and '_parameter' naming conventions
        return self._object
    
    def after(self):
        #helper function to read next in sequence value
        #if nothing is next, return's itself
        if self._next != None:
            return self._next
        return self
    
    def before(self):
        #helper function to read previous in sequence value
        #if nothing is previous, return's itself
        if self._prev != None:
            return self._prev
        return self
    
    def append(self, obj):
        #adds a new Item to the list
        if self._object == None:
            #first checks if the list is empty and fills it if so
            self._object = obj
            newItem = self
        else:
            #if something is already in the list, 
            #find the end of the list and add the new item
            last = self.last()
            
            newItem = Item(obj)
            newItem._prev = last
            last._next = newItem
        return newItem #returns the end of the list
    
    def prepend(self, obj):
        #same behavior as append but adds to the start of the list
        if self._object == None:
            self._object = obj
            newItem = self
        else:
            first = self.first()
            newItem = Item(obj)
            newItem._next = first
            first._prev = newItem
        #returns the start of the list instead of the end list append
        return newItem 
        
    def last(self):
        #finds and returns the end of the list
        iter = self
        while True:
            if iter._next == None:
                break
            iter = iter._next
        return iter
    
    def first(self):
        #finds and returns the start of the list
        iter = self
        while True:
            if iter._prev == None:
                break
            iter = iter._prev
        return iter
    
    def insertAfter(self, obj):
        #rather than appending to the end, this will squeeze
        #the new item into the next position from self's 
        #current position in the list
        if self._object == None:
            #checks for an empty list first
            self._object = obj
            newItem = self
        else:
            #for a non-empty list
            newItem = Item(obj)
            if self._next != None:
                #I modified this part.  the same assignments were 
                #being made to newitem._prev and self._next
                #and as long as they happened after the conditional
                #part the result was the same - so no else statement anymore
                newItem._next = self._next
                self._next._prev = newItem
            newItem._prev = self
            self._next = newItem
        return newItem
    
    def insertBefore(self, obj):
        #same as above but squeezed into the previous position
        if self._object == None:
            self._object = obj
            newItem = self
        else:
            newItem = Item(obj)
            if self._prev != None:
                #same modification as above
                newItem._prev = self._prev
                self._prev._next = newItem
            newItem._next = self
            self._prev = newItem
        return newItem
    
    def extract(self):
        #effectively deletes the current list item from the rest of the list
        rest = None
        if self._prev == None and self._next == None:
            #if there is nothing else in the list, return a new empty list
            rest = Item( )
        else:
            #if the code gets here, one or both of _prev and _next are present
            if self._prev == None:
                #self is the first item in the list, erase self from the next item
                #and return that item
                self._next._prev = None
                rest = self._next
            else:
                if self._next == None:
                    #self is at the end of the list, erase self from
                    #the previous item and return that item
                    self._prev._next = None
                    rest = self._next
                else:
                    #self is in the middle of the list, erase it from
                    #the previous and next items and introduce them 
                    #to each other
                    self._prev._next = self._next
                    self._next._prev = self._prev
                    rest = self._prev
        #I don't think these two lines are necessary
        #self._prev = None
        #self._next = None
        return rest
        
    def forEach(self, caller):
        #do something to every item in the list, from first to last
        iter = self.first( )
        while True:
            #.withItem is part of the Stand class in fruit.py
            #it prints "with: " + the object passed
            caller.withItem(iter._object) 
            if iter._next == None: #if the end of the list is reached
                break
            #the code can only get there if there is a next item
            iter = iter._next
    
    def __iter__(self):
        #returns an iterable object (an object with a __next__ method)
        
        head = self.first( )
        head._iter = head
        return head._iter
                
    def __next__(self):
        #in this case, self is the iterable object returned by __iter__
        #but it is an instance variable and keeps its parameter values 
        #through each call, allowing the iteration to work
        
        head = self.first( )
        if head._iter == None:
            raise StopIteration
        target = head._iter._object
        head._iter = head._iter._next
        return target
            
    def count(self):
        #counts the items in the list by first finding the start of the
        #list and then stepping forward
        iter = self.first( )
        if iter._object == None:
            #checking for an empty list
            count = 0
        else:
            #otherwise start counting
            count = 1
        while True:
            if iter._next == None: #at the end of the list this will be True
                break
            #if it gets here, add another to the count and move to the next list item
            iter = iter._next
            count += 1
        return count
    
    def at(self, n): 
        #returns the list item at position n
        iter = self.first( )
        if iter._object != None:
            count = 0
            while count < n:
                if iter._next == None:
                    iter = None
                    raise Exception( "Index beyond end." )
                iter = iter._next
                count += 1
        return iter
    
    def has(self, obj):
        #checks if an item object is part of the list
        #returns that item if it is and None if not
        if self._object != None:
            iter = self.first ( )
            while iter != None:
                if iter._object == obj:
                    break
                iter = iter._next
        else:
            iter = None
        return iter
    
    def clear(self):
        #clears the entire list - I feel like this would be less
        #confusing if instead of the iter, we just reassigned self
        #to self.first()
        iter = self.first( )
        while iter._next is not None:
            #from the first item in the list, if not the last item
            #then go to the next item and erase everything from the 
            #previous one
            iter = iter._next
            print( f"clearing: {iter._prev._object}" )
            iter._prev._prev = None
            iter._prev._next = None
            iter._prev._object = None
        print( f"clearing: {iter._object}" )
        iter._prev = None
        iter._object = None
    
    def toList(self):
        #makes a python list from our Item class object
        list = []
        iter = self.first( )
        if iter._object is not None:
            #checks to see if there is at least one thing in the Item list
            while True:
                #adds it then any subsequent Item in the list to the python list
                list.append(iter._object)
                if iter._next == None:
                    #if the end is reached, stop
                    break
                iter = iter._next
        return list
    
    def fromList(self, list):
        #adds items from a python list onto the end of the Item list object
        print(f'self: {self}')
        for item in list:
            self.append(item)
    
