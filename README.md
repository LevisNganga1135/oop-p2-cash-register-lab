# Cash Register — OOP Lab

A Python implementation of a cash register for an e-commerce site, built using Object Oriented Programming principles including classes, properties, and encapsulation.

---

## Table of Contents

- [Overview](#overview)
- [Class Structure](#class-structure)
- [Attributes](#attributes)
- [Properties](#properties)
- [Methods](#methods)
- [Usage Examples](#usage-examples)
- [Setup](#setup)

---

## Overview

The `CashRegister` class simulates the core functionality of a cash register. It allows you to:

- Add items with a name, price, and quantity
- Apply a percentage discount to the running total
- Void the last transaction
- Track all items and transaction history

---

## Class Structure

```
CashRegister
│
├── Attributes
│   ├── discount
│   ├── total
│   ├── items
│   └── previous_transactions
│
├── Properties
│   └── discount (getter + setter with validation)
│
└── Methods
    ├── add_item(item, price, quantity)
    ├── apply_discount()
    └── void_last_transaction()
```

---

## Attributes

| Attribute               | Type    | Default | Description                                          |
|-------------------------|---------|---------|------------------------------------------------------|
| `discount`              | `int`   | `0`     | Percentage discount to apply to the total (0–100)    |
| `total`                 | `float` | `0`     | Running total of all items added                     |
| `items`                 | `list`  | `[]`    | List of item names currently in the register         |
| `previous_transactions` | `list`  | `[]`    | Log of all transactions as dicts (item, price, qty)  |

---

## Properties

### `discount`

Validates the discount value on assignment.

- Must be an **integer**
- Must be **between 0 and 100 inclusive**
- Prints `"Not valid discount"` and resets to `0` if validation fails

```python
register.discount = 20    # valid — sets discount to 20
register.discount = 150   # invalid — prints "Not valid discount", resets to 0
register.discount = 10.5  # invalid — prints "Not valid discount", resets to 0
```

---

## Methods

### `add_item(item, price, quantity=1)`

Adds an item to the cash register.

| Parameter  | Type    | Default | Description                        |
|------------|---------|---------|------------------------------------|
| `item`     | `str`   | —       | Name of the item                   |
| `price`    | `float` | —       | Price per single unit              |
| `quantity` | `int`   | `1`     | Number of units being purchased    |

- Adds `price × quantity` to `self.total`
- Appends the item name to `self.items`
- Logs a dict `{ item, price, quantity }` to `self.previous_transactions`

---

### `apply_discount()`

Applies the discount percentage to the current total.

- Deducts `(discount / 100) × total` from `self.total`
- Removes the last transaction from `previous_transactions`
- Removes the corresponding item from `items`
- Prints `"There is no discount to apply."` if no transactions exist

---

### `void_last_transaction()`

Reverses the most recent transaction.

- Subtracts `price × quantity` of the last transaction from `self.total`
- Removes the item from `self.items`
- Removes the transaction from `self.previous_transactions`
- Prints `"There are no transactions to void."` if no transactions exist

---

## Usage Examples

```python
from cash_register import CashRegister

# Create a register with a 20% discount
register = CashRegister(20)

# Add items
register.add_item("Apple", 1.50, 4)   # 4 apples at $1.50 each
register.add_item("Bread", 3.00)       # 1 bread at $3.00
register.add_item("Milk", 2.50, 2)    # 2 milks at $2.50 each

print(register.total)   # 15.0
print(register.items)   # ['Apple', 'Bread', 'Milk']

# Apply discount
register.apply_discount()
# Output: After the discount, the total comes to $12.00

# Void the last transaction
register.void_last_transaction()
# Output: Voided: Bread. New total: $9.00

# Invalid discount
register.discount = 200
# Output: Not valid discount
```

---

## Setup

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd <repo-folder>
   ```

2. No external dependencies required — uses only Python's standard library.

3. Run the file directly:
   ```bash
   python cash_register.py
   ```

4. Or import the class into your own script:
   ```python
   from cash_register import CashRegister
   ```

---

## Author

Built as part of the **Object Oriented Programming Part 2** lab at **Moringa School**.