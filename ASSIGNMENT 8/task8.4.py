# ✅ Implementation of ShoppingCart class that passes all tests

class ShoppingCart:
    """A simple shopping cart to add, remove, and total items."""

    def __init__(self):
        # Store items as a dictionary: {item_name: price}
        self.items = {}

    def add_item(self, name: str, price: float) -> None:
        """Add an item with its price to the cart."""
        # Validation: ensure price is numeric and positive
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a positive number.")
        self.items[name] = price

    def remove_item(self, name: str):
        """Remove item from the cart if it exists."""
        if name in self.items:
            del self.items[name]
        else:
            # Return None (graceful handling for missing item)
            return None

    def total_cost(self) -> float:
        """Calculate total cost of all items in the cart."""
        return sum(self.items.values())






def run_tests() -> None:
	"""
	AI-generated functional tests for a `ShoppingCart` class with the contract:
	- `add_item(name, price)` adds an item (price is numeric) to the cart.
	- `remove_item(name)` removes a previously added item identified by `name`.
	- `total_cost()` returns the aggregated cost of the items currently in the cart.
	"""
	try:
		ShoppingCart  # type: ignore[name-defined]
	except NameError:
		print("ShoppingCart class is not defined. Please implement it before running tests.")
		return

	tests = []

	def test_empty_cart_total_is_zero() -> None:
		cart = ShoppingCart()  # type: ignore[call-arg]
		assert cart.total_cost() == 0, "Expected empty cart to have total cost 0"

	tests.append(("empty cart total is zero", test_empty_cart_total_is_zero))

	def test_add_items_accumulates_total() -> None:
		cart = ShoppingCart()  # type: ignore[call-arg]
		cart.add_item("apple", 120)
		cart.add_item("banana", 80)
		cart.add_item("coffee", 450)
		assert cart.total_cost() == 650, "Total cost should sum all added item prices (120+80+450)"

	tests.append(("add_item accumulates total", test_add_items_accumulates_total))

	def test_remove_item_updates_total() -> None:
		cart = ShoppingCart()  # type: ignore[call-arg]
		cart.add_item("apple", 150)
		cart.add_item("bread", 250)
		cart.add_item("cheese", 300)
		cart.remove_item("bread")
		assert cart.total_cost() == 450, "Removing 'bread' (250) should reduce total to 150+300"

	tests.append(("remove_item updates total", test_remove_item_updates_total))

	def test_remove_missing_item_is_graceful() -> None:
		cart = ShoppingCart()  # type: ignore[call-arg]
		cart.add_item("milk", 200)
		try:
			result = cart.remove_item("eggs")
		except (KeyError, ValueError, LookupError):
			pass  # acceptable ways to signal missing item
		except Exception as ex:
			raise AssertionError(f"Unexpected exception type when removing missing item: {type(ex).__name__}: {ex}") from ex
		else:
			assert result in (None, False), "Removing a missing item should return None/False if not raising an exception"
		assert cart.total_cost() == 200, "Failed removal must not alter existing items"

	tests.append(("remove_item handles missing entries", test_remove_missing_item_is_graceful))

	def test_multiple_add_remove_sequence() -> None:
		cart = ShoppingCart()  # type: ignore[call-arg]
		cart.add_item("pen", 50)
		cart.add_item("notebook", 200)
		cart.add_item("eraser", 30)
		cart.remove_item("pen")
		cart.add_item("marker", 120)
		cart.remove_item("eraser")
		assert cart.total_cost() == 320, "Sequence should leave notebook (200) + marker (120)"

	tests.append(("mixed add/remove sequence", test_multiple_add_remove_sequence))

	total = len(tests)
	passed = 0

	for description, test in tests:
		try:
			test()
			passed += 1
		except AssertionError as ex:
			print(f"FAIL: {description} -> {ex}")
		except Exception as ex:
			print(f"EXCEPTION: {description} -> {type(ex).__name__}: {ex}")

	print(f"Passed {passed}/{total} tests")


if __name__ == "__main__":
	run_tests()


# ✅ Inline safeguard before running tests

