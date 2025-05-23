print ("--------------------------------------------------------------------------")
print("Welcome to Circular Buffer Implementation in Python\n"
      "Written by Tomer Elis")
print ("--------------------------------------------------------------------------\n")


class CircularBuffer:
    def __init__(self, size):

        # Check if size is a positive integer
        while not isinstance(size, int) or size <= 0:
            try:
                size = int(input("Enter buffer size (positive integer): "))
                if size <= 0:
                    print("Size must be greater than 0.")
            except ValueError:
                print("Size must be an integer. Please try again.")


        self.buffer = [None] * size
        self.size = size
        self.head = 0
        self.tail = 0
        self.count = 0

    def push(self, item):
        if self.is_full():
            #overwrite the oldest item
            print("Buffer is full. Overwriting the oldest item (tail).")
            self.buffer[self.tail] = None
            self.buffer[self.tail] = item
            self.tail = (self.tail + 1) % self.size
            self.head = (self.head + 1) % self.size
            self.count = self.size          #safety
            print(f"Pushed item: {item}")
        else:
            self.buffer[self.head] = item
            self.head = (self.head + 1) % self.size
            self.count += 1
            print(f"Pushed item: {item}")

    def pop(self):
        if self.is_empty():
            print("Buffer is empty. Cannot pop.")
            return None
        else:
            item = self.buffer[self.tail]
            self.buffer[self.tail] = None
            self.tail = (self.tail + 1) % self.size
            self.count -= 1
            print(f"Popped item: {item}")
            return item


    def peek(self):
        if self.is_empty():
            print("Buffer is empty. Cannot peek.")
            return None
        else:
            item = self.buffer[self.tail]
            print(f"Peeked item: {item}")
            return item

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size


    def resize(self, new_size):

        #check if new size is a positive integer
        while not isinstance(new_size, int) or new_size <= 0:
            try:
                new_size = int(input("Enter new buffer size (positive integer): "))
                if new_size <= 0:
                    print("Size must be greater than 0.")
            except ValueError:
                print("Size must be an integer. Please try again.")

        if new_size <= 0:
            print("Size must be greater than 0. Cannot resize.")
            return
        # Keep the most recent N items if shrinking
        items_to_keep = min(self.count, new_size)
        start_index = (self.tail + self.count - items_to_keep) % self.size

        # Create a new buffer with the new size
        new_buffer = [None] * new_size
        for i in range(min(self.count, new_size)):
            new_buffer[i] = self.buffer[(start_index + i) % self.size]
        self.buffer = new_buffer
        self.size = new_size
        self.tail = 0
        self.count = min(self.count, new_size)
        self.head = self.count % new_size

    def __str__(self):  # String representation of the buffer head and tail
        return f"Buffer: {self.buffer}, Head: {self.head}, Tail: {self.tail}, Count: {self.count}"


