def find_common(a, b):
    return list(set(a) & set(b))
    def find_common_fast(a, b):
        """Returns common elements (unordered) between two lists using set intersection."""
        return list(set(a) & set(b))

    def find_common_ordered(a, b):
        """Returns common elements (preserving order from list a)."""
        set_b = set(b)
        return [x for x in a if x in set_b]

# Example usage:
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

print("Common elements:", find_common(list1, list2))
print("Common elements with [10, 11, 4]:", find_common(list1, [10, 11, 4]))
print("Common elements with [2, 3, 8]:", find_common(list1, [2, 3, 8]))

