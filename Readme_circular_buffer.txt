Design Diary

Design Decision:
used a list to represent the buffer.
maintained head, tail, and count variables to track buffer state and support circular indexing.




Main Design Decisions:

The main idea behind this design was to allow the user to keep working without interruptions or the need for troubleshooting.
Therefore, the buffer allows continuous addition of values by automatically overwriting the oldest ones, following the FIFO (First In, First Out) principle.

- The head points to where the next item will be inserted (youngest).
- The tail points to the oldest item in the buffer.
If the circular buffer reaches its maximum capacity and the user continue pushing new values, the oldest value (tail) will be overwritten by the new value.

The head and tail pointers update accordingly to maintain the circular structure.
When the buffer is resized (especially reduced in size), only the most recent (youngest) values are kept. The older values are discarded to fit the new size.



Edge Cases Handled:
Full buffer overwrite - Oldest item is automatically replaced when pushing to a full buffer.
Popping from empty buffer - Returns None and displays a message without crashing.
Mix of data types - strings and numbers, Handled without errors.
Resize with data - Keeps most recent values when reducing buffer size.


Improvements 
The __str__ method is used for debugging and testing. It provides a live status of the buffer, including the head, tail, and count values.
More details about the internal flow can be found in the FMS drawing module.

The FSM (Finite State Machine) module can be found in the Word document.
