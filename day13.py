from pprint import pprint
import json
from enum import IntEnum
from functools import cmp_to_key
from copy import deepcopy

## Part 1

# Read input
packet_pairs = open("day13input.txt", "r", encoding="utf-8").read().strip().split("\n")

first_packet = ""
second_packet = ""
current_pair = 1
pairs = []


class Comparison(IntEnum):
    """An IntEnum representing comparison results.
    IN_ORDER is -1 (left < right)
    NEXT_NUMBER is 0 (left == right)
    NOT_IN_ORDER is 1 (left > right)

    Helpful for sorting.
    """

    IN_ORDER = -1
    NEXT_NUMBER = 0
    NOT_IN_ORDER = 1


def compare_elems(first_elem, second_elem):
    """A function that compares two elements of a list.

    Args:
        first_elem (int || list): The left element
        second_elem (int || list): The right element

    Returns:
        Comparison: whether or not the elements are in order or not.
    """
    # the simplest comparison (int with int)
    if isinstance(first_elem, int) and isinstance(second_elem, int):
        if first_elem < second_elem:
            return Comparison.IN_ORDER
        if first_elem == second_elem:
            return Comparison.NEXT_NUMBER
        if first_elem > second_elem:
            return Comparison.NOT_IN_ORDER
    # otherwise, compare the two elements as lists
    # this will convert both to lists
    if isinstance(first_elem, int) and isinstance(second_elem, list):
        return compare_elems([first_elem], second_elem)
    # this will also convert both to lists
    if isinstance(first_elem, list) and isinstance(second_elem, int):
        return compare_elems(first_elem, [second_elem])
    # if we've run out of elements in the left list, but not the right, we're in order.
    if len(first_elem) == 0 and len(second_elem) != 0:
        return Comparison.IN_ORDER
    comparison_state = Comparison.NEXT_NUMBER
    # otherwise, iterate over the elements in the list
    for first_item_index, first_item in enumerate(first_elem):
        # if the first list ends up longer than the second list after
        # it not being in order before, it's not in order
        if first_item_index >= len(second_elem):
            return Comparison.NOT_IN_ORDER
        second_item = second_elem[first_item_index]
        # compare the elements of the first_elem and second_elem lists.
        comparison_state = compare_elems(first_item, second_item)
        # if it's IN_ORDER or NOT_IN_ORDER, return
        if comparison_state != Comparison.NEXT_NUMBER:
            return comparison_state
        # if it's been equal, and we're at the last item in the left
        # list, and the right list is longer, we're in order.
        if (
            comparison_state == Comparison.NEXT_NUMBER
            and first_item_index == len(first_elem) - 1
            and len(first_elem) < len(second_elem)
        ):
            return Comparison.IN_ORDER
    return comparison_state


# Parse pairs
for packet_line_index, packet_line in enumerate(packet_pairs):
    if packet_line_index % 3 == 0:
        first_packet = json.loads(packet_line)
    if packet_line_index % 3 == 1:
        second_packet = json.loads(packet_line)
    if packet_line_index % 3 == 2:  # compare packets
        result = compare_elems(first_packet, second_packet)
        pair = {
            "index": current_pair,
            "first_packet": deepcopy(first_packet),
            "second_packet": deepcopy(second_packet),
            "in_order": result == Comparison.IN_ORDER,
        }
        pairs.append(pair)
        current_pair += 1
# capture the last pair
result = compare_elems(first_packet, second_packet)
pair = {
    "index": current_pair,
    "first_packet": deepcopy(first_packet),
    "second_packet": deepcopy(second_packet),
    "in_order": result == Comparison.IN_ORDER,
}
pairs.append(pair)

summed_in_order_pair_indexes = 0
for pair in pairs:
    if pair["in_order"]:
        summed_in_order_pair_indexes += pair["index"]
print(f"Part 1: {summed_in_order_pair_indexes}")

## Part 2

flattened = []

for pair in pairs:
    flattened.extend([pair["first_packet"], pair["second_packet"]])
flattened.extend([[[2]], [[6]]])

# I love python. We just have functions that sort based on a function you've already written 🤣
flattened.sort(key=cmp_to_key(compare_elems))
print(f"Part 2: {(flattened.index([[2]]) + 1) * (flattened.index([[6]]) + 1)}")
