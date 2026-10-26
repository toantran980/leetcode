# LeetCode Solutions

A collection of Python solutions to common LeetCode and interview problems. Each solution is in its own file and generally follows the LeetCode `Solution` class format. Some files rely on types or helpers provided by the online judge, such as `ListNode`, `TreeNode`, and `Interval`.

## Solutions

- **Arrays and hashing:** `best_time_to_buy_and_sell_stock.py`, `contains_duplicate.py`, `group_anagrams.py`, `maximum_subarray.py`, `missing_number.py`, `plus_one.py`, `single_number.py`, `top_k_frequent_elements.py`, `two_sum.py`, `valid_anagram.py`
- **Binary search and bit manipulation:** `binary_search.py`, `counting_bits.py`, `number_of_1_bits.py`, `reverse_bits.py`
- **Strings and stacks:** `valid_palindrome.py`, `valid_parentheses.py`
- **Dynamic programming:** `climbing_stairs.py`, `min_cost_climbing_stars.py`
- **Trees:** `balanced_binary_tree.py`, `diameter_of_binary_tree.py`, `invert_binary_tree.py`, `maximum_of_binary_tree.py`, `same_binary_tree.py`, `subtree_of_another_tree.py`
- **Linked lists:** `linked_list_cycle.py`, `merge_two_sorted_linked_lists.py`, `reverse_linked_list.py`
- **Heaps and scheduling:** `kth_largest_elemen_in_a_stream.py`, `last_stone_weight.py`, `meeting_rooms.py`
- **Other:** `happy_number.py`, `top_k_sample.py`

## Tests

Run the unit tests from the repository root:

```bash
python -m unittest discover -s tests -v
```

The tests use Python's standard-library `unittest` framework. PyTorch is also required because `top_k_sample.py` implements top-k sampling with tensors.
