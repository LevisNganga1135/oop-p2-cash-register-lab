class CashRegister:
    """
    Simulates a cash register for an e-commerce site.
    Supports adding items, applying discounts, and voiding transactions.
    """

    def __init__(self, discount=0):
        """
        Initialize the CashRegister with an optional discount.

        Args:
            discount (int): Percentage discount to apply (0-100). Defaults to 0.
        """
        self.discount = discount             # uses the property setter for validation
        self.total = 0                       # running total of all added items
        self.items = []                      # list of item names (one entry per unit)
        self.previous_transactions = []      # log of every transaction as a dict

    # ── Discount property ──────────────────────────────────────────────────

    @property
    def discount(self):
        """Return the current discount percentage."""
        return self._discount

    @discount.setter
    def discount(self, value):
        """
        Validate and set the discount percentage.
        - Must be an integer.
        - Must be between 0 and 100 inclusive.
        Prints 'Not valid discount' and resets to 0 if validation fails.
        """
        if not isinstance(value, int):
            # reject non-integer values (e.g. floats, strings)
            print("Not valid discount")
            self._discount = 0
        elif 0 <= value <= 100:
            # valid range — store the value
            self._discount = value
        else:
            # out of range (negative or above 100)
            print("Not valid discount")
            self._discount = 0

    # ── Methods ────────────────────────────────────────────────────────────

    def add_item(self, item, price, quantity=1):
        """
        Add an item to the cash register.

        Args:
            item (str): Name of the item being purchased.
            price (float): Price of a single unit of the item.
            quantity (int): Number of units being purchased. Defaults to 1.

        Note:
            Each unit is added as a separate entry in self.items so that
            void_last_transaction can correctly remove all units at once.
        """
        # calculate the total cost for this line (price × quantity)
        line_total = price * quantity

        # add the line total to the running register total
        self.total += line_total

        # add one entry per unit so items reflects individual quantities
        # e.g. add_item("egg", 1.99, 2) → ["egg", "egg"]
        self.items.extend([item] * quantity)

        # log the full transaction details for future reference
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        """
        Apply the discount percentage to the current total.
        - Prints an error message if no discount is set (discount == 0).
        - Deducts (discount %) from self.total.
        - Removes the last transaction and its item entries from their lists.
        - Prints a success message with the updated total.
        """
        # guard: no discount is set on this register
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        # calculate discount amount as a percentage of the current total
        discount_amount = self.total * (self.discount / 100)

        # subtract the discount from the running total
        self.total -= discount_amount

        # remove the last transaction from the log
        last = self.previous_transactions.pop()

        # remove all unit entries for the last item from the items list
        for _ in range(last["quantity"]):
            self.items.remove(last["item"])

        # format without trailing zeros e.g. $800. not $800.00
        formatted = f"${self.total:g}" if self.total == int(self.total) else f"${self.total:.2f}"
        print(f"After the discount, the total comes to {formatted}.")

    def void_last_transaction(self):
        """
        Reverse the most recent transaction.
        - Subtracts the last transaction's value from self.total.
        - Removes all unit entries of that item from self.items.
        - Removes the transaction from self.previous_transactions.
        - Prints a message if there are no transactions to void.
        """
        # guard: nothing to void if no transactions exist
        if not self.previous_transactions:
            print("There are no transactions to void.")
            return

        # pop the last transaction off the log
        last = self.previous_transactions.pop()

        # reverse its effect on the total (price × quantity)
        self.total -= last["price"] * last["quantity"]

        # remove all unit entries for this item from the items list
        for _ in range(last["quantity"]):
            self.items.remove(last["item"])