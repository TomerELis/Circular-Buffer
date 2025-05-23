# Circular Buffer in Python (OOP)

Implemented a **circular buffer** in Python using **object-oriented programming**.  
Designed a custom `CircularBuffer` class with methods for `push`, `pop`, `peek`, and dynamic `resize`.

<img src="https://github.com/user-attachments/assets/949cddb1-846b-4237-abc7-7853a4070a4a" width="400"/>


---

## Design Decisions

- Used a Python `list` to represent the buffer.
- Maintained `head`, `tail`, and `count` to track state and support circular indexing.
- Automatically overwrites the oldest data when full (FIFO logic).
- `head` points to the next insertion (youngest).
- `tail` points to the oldest item.
- On resize (especially shrink), keeps only the most recent values.

---

## Edge Cases Handled

- **Full buffer overwrite**: Replaces the oldest item when pushing to a full buffer.
- **Pop/peek from empty buffer**: Returns `None` and shows a message without crashing.
- **Mixed data types**: Supports both strings and numbers without errors.
- **Resize with data**: Keeps most recent items when reducing buffer size.

---

## 🛠 Improvements

- Added `__str__()` for debugging – shows buffer, head, tail, and count.
- Internal logic explained in the FSM (Finite State Machine) module.
- FSM diagram and further flow details are available in the attached Word document.
