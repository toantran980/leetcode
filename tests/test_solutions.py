import heapq
import importlib.util
import unittest
from collections import Counter, defaultdict
from pathlib import Path
from typing import List, Optional

import torch


ROOT = Path(__file__).resolve().parents[1]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def load_solution(filename):
    path = ROOT / filename
    spec = importlib.util.spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load {filename}")

    module = importlib.util.module_from_spec(spec)
    module.__dict__.update(
        {
            "Counter": Counter,
            "Interval": Interval,
            "List": List,
            "ListNode": ListNode,
            "Optional": Optional,
            "TreeNode": TreeNode,
            "defaultdict": defaultdict,
            "heapq": heapq,
        }
    )
    spec.loader.exec_module(module)
    return module


class SolutionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        filenames = (
            "balanced_binary_tree.py",
            "best_time_to_buy_and_sell_stock.py",
            "binary_search.py",
            "climbing_stairs.py",
            "contains_duplicate.py",
            "counting_bits.py",
            "diameter_of_binary_tree.py",
            "group_anagrams.py",
            "happy_number.py",
            "invert_binary_tree.py",
            "kth_largest_elemen_in_a_stream.py",
            "last_stone_weight.py",
            "linked_list_cycle.py",
            "maximum_of_binary_tree.py",
            "maximum_subarray.py",
            "meeting_rooms.py",
            "merge_two_sorted_linked_lists.py",
            "min_cost_climbing_stars.py",
            "missing_number.py",
            "number_of_1_bits.py",
            "plus_one.py",
            "reverse_bits.py",
            "reverse_linked_list.py",
            "same_binary_tree.py",
            "single_number.py",
            "subtree_of_another_tree.py",
            "top_k_frequent_elements.py",
            "top_k_sample.py",
            "two_sum.py",
            "valid_anagram.py",
            "valid_palindrome.py",
            "valid_parentheses.py",
        )
        cls.modules = {filename: load_solution(filename) for filename in filenames}

    def solution(self, filename):
        return self.modules[filename].Solution()

    def test_balanced_binary_tree(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4))
        self.assertTrue(self.solution("balanced_binary_tree.py").isBalanced(root))
        self.assertTrue(self.solution("balanced_binary_tree.py").isBalanced(None))
        unbalanced = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
        self.assertFalse(self.solution("balanced_binary_tree.py").isBalanced(unbalanced))

    def test_best_time_to_buy_and_sell_stock(self):
        solver = self.solution("best_time_to_buy_and_sell_stock.py")
        self.assertEqual(solver.maxProfit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(solver.maxProfit([7, 6, 4, 3, 1]), 0)
        self.assertEqual(solver.maxProfit([]), 0)

    def test_binary_search(self):
        solver = self.solution("binary_search.py")
        self.assertEqual(solver.search([-1, 0, 3, 5, 9, 12], 9), 4)
        self.assertEqual(solver.search([-1, 0, 3, 5, 9, 12], 2), -1)
        self.assertEqual(solver.search([], 4), -1)

    def test_climbing_stairs(self):
        solver = self.solution("climbing_stairs.py")
        self.assertEqual(solver.climbStairs(1), 1)
        self.assertEqual(solver.climbStairs(2), 2)
        self.assertEqual(solver.climbStairs(5), 8)

    def test_contains_duplicate(self):
        solver = self.solution("contains_duplicate.py")
        self.assertTrue(solver.hasDuplicate([1, 2, 3, 1]))
        self.assertFalse(solver.hasDuplicate([1, 2, 3, 4]))
        self.assertFalse(solver.hasDuplicate([]))

    def test_counting_bits(self):
        solver = self.solution("counting_bits.py")
        self.assertEqual(solver.countBits(0), [0])
        self.assertEqual(solver.countBits(5), [0, 1, 1, 2, 1, 2])

    def test_diameter_of_binary_tree(self):
        solver = self.solution("diameter_of_binary_tree.py")
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        self.assertEqual(solver.diameterOfBinaryTree(root), 3)
        self.assertEqual(solver.diameterOfBinaryTree(TreeNode(1)), 0)
        self.assertEqual(solver.diameterOfBinaryTree(None), 0)

    def test_group_anagrams(self):
        groups = self.solution("group_anagrams.py").groupAnagrams(
            ["eat", "tea", "tan", "ate", "nat", "bat"]
        )
        self.assertEqual({frozenset(group) for group in groups}, {
            frozenset({"eat", "tea", "ate"}),
            frozenset({"tan", "nat"}),
            frozenset({"bat"}),
        })
        self.assertEqual(self.solution("group_anagrams.py").groupAnagrams([]), [])

    def test_happy_number(self):
        solver = self.solution("happy_number.py")
        self.assertTrue(solver.isHappy(19))
        self.assertFalse(solver.isHappy(2))
        self.assertEqual(solver.sumOfSquares(123), 14)

    def test_invert_binary_tree(self):
        solver = self.solution("invert_binary_tree.py")
        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
        result = solver.invertTree(root)
        self.assertIs(result, root)
        self.assertEqual(result.left.val, 7)
        self.assertEqual((result.right.left.val, result.right.right.val), (3, 1))
        self.assertIsNone(solver.invertTree(None))

    def test_kth_largest_element_in_a_stream(self):
        kth_largest = self.modules["kth_largest_elemen_in_a_stream.py"].KthLargest(
            3, [4, 5, 8, 2]
        )
        self.assertEqual(kth_largest.add(3), 4)
        self.assertEqual(kth_largest.add(5), 5)
        self.assertEqual(kth_largest.add(10), 5)
        self.assertEqual(kth_largest.add(9), 8)
        self.assertEqual(kth_largest.add(4), 8)

    def test_last_stone_weight(self):
        solver = self.solution("last_stone_weight.py")
        self.assertEqual(solver.lastStoneWeight([2, 7, 4, 1, 8, 1]), 1)
        self.assertEqual(solver.lastStoneWeight([3, 3]), 0)
        self.assertEqual(solver.lastStoneWeight([]), 0)

    def test_linked_list_cycle(self):
        solver = self.solution("linked_list_cycle.py")
        first, second, third = ListNode(1), ListNode(2), ListNode(3)
        first.next, second.next = second, third
        self.assertFalse(solver.hasCycle(first))
        third.next = second
        self.assertTrue(solver.hasCycle(first))
        self.assertFalse(solver.hasCycle(None))

    def test_maximum_of_binary_tree_depth(self):
        solver = self.solution("maximum_of_binary_tree.py")
        root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
        self.assertEqual(solver.maxDepth(root), 3)
        self.assertEqual(solver.maxDepth(None), 0)

    def test_maximum_subarray(self):
        solver = self.solution("maximum_subarray.py")
        self.assertEqual(solver.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(solver.maxSubArray([-3, -1, -2]), -1)
        self.assertEqual(solver.maxSubArray([5]), 5)

    def test_meeting_rooms(self):
        solver = self.solution("meeting_rooms.py")
        self.assertTrue(solver.canAttendMeetings([]))
        self.assertTrue(
            solver.canAttendMeetings([Interval(0, 10), Interval(10, 20)])
        )
        self.assertFalse(
            solver.canAttendMeetings([Interval(0, 30), Interval(5, 10)])
        )

    def test_merge_two_sorted_linked_lists(self):
        solver = self.solution("merge_two_sorted_linked_lists.py")
        first = ListNode(1, ListNode(2, ListNode(4)))
        second = ListNode(1, ListNode(3, ListNode(4)))
        self.assertEqual(self.list_values(solver.mergeTwoLists(first, second)), [1, 1, 2, 3, 4, 4])
        self.assertEqual(self.list_values(solver.mergeTwoLists(None, None)), [])

    def test_min_cost_climbing_stairs(self):
        solver = self.solution("min_cost_climbing_stars.py")
        self.assertEqual(solver.minCostClimbingStairs([10, 15, 20]), 15)
        self.assertEqual(
            solver.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]),
            6,
        )
        self.assertEqual(solver.minCostClimbingStairs([]), 0)

    def test_missing_number(self):
        solver = self.solution("missing_number.py")
        self.assertEqual(solver.missingNumber([3, 0, 1]), 2)
        self.assertEqual(solver.missingNumber([0, 1]), 2)
        self.assertEqual(solver.missingNumber([]), 0)

    def test_number_of_1_bits(self):
        solver = self.solution("number_of_1_bits.py")
        self.assertEqual(solver.hammingWeight(0b00000000000000000000000000001011), 3)
        self.assertEqual(solver.hammingWeight(0), 0)

    def test_plus_one(self):
        solver = self.solution("plus_one.py")
        self.assertEqual(solver.plusOne([1, 2, 3]), [1, 2, 4])
        self.assertEqual(solver.plusOne([1, 2, 9]), [1, 3, 0])
        self.assertEqual(solver.plusOne([9, 9, 9]), [1, 0, 0, 0])

    def test_reverse_bits(self):
        solver = self.solution("reverse_bits.py")
        self.assertEqual(solver.reverseBits(43261596), 964176192)
        self.assertEqual(solver.reverseBits(0), 0)

    def test_reverse_linked_list(self):
        solver = self.solution("reverse_linked_list.py")
        reversed_head = solver.reverseList(ListNode(1, ListNode(2, ListNode(3))))
        self.assertEqual(self.list_values(reversed_head), [3, 2, 1])
        self.assertIsNone(solver.reverseList(None))
        singleton = ListNode(7)
        self.assertIs(solver.reverseList(singleton), singleton)

    def test_same_binary_tree(self):
        solver = self.solution("same_binary_tree.py")
        tree = TreeNode(1, TreeNode(2), TreeNode(3))
        same_tree = TreeNode(1, TreeNode(2), TreeNode(3))
        different_tree = TreeNode(1, TreeNode(2), None)
        self.assertTrue(solver.isSameTree(tree, same_tree))
        self.assertFalse(solver.isSameTree(tree, different_tree))
        self.assertTrue(solver.isSameTree(None, None))

    def test_single_number(self):
        solver = self.solution("single_number.py")
        self.assertEqual(solver.singleNumber([2, 2, 1]), 1)
        self.assertEqual(solver.singleNumber([4, 1, 2, 1, 2]), 4)

    def test_subtree_of_another_tree(self):
        solver = self.solution("subtree_of_another_tree.py")
        root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
        subtree = TreeNode(4, TreeNode(1), TreeNode(2))
        self.assertTrue(solver.isSubtree(root, subtree))
        self.assertFalse(solver.isSubtree(root, TreeNode(4, TreeNode(1), None)))
        self.assertTrue(solver.isSubtree(root, None))
        self.assertFalse(solver.isSubtree(None, TreeNode(1)))

    def test_top_k_frequent_elements(self):
        solver = self.solution("top_k_frequent_elements.py")
        result = solver.topKFrequent([1, 1, 1, 2, 2, 3], 2)
        self.assertEqual(set(result), {1, 2})
        self.assertEqual(solver.topKFrequent([5], 1), [5])

    def test_top_k_sample(self):
        solver = self.solution("top_k_sample.py")
        logits = torch.tensor([2.0, 1.0, 0.1, 0.5])
        self.assertEqual(solver.top_k_sample(logits, k=1), 0)
        self.assertIn(solver.top_k_sample(logits, k=2), {0, 1})
        self.assertIn(solver.top_k_sample(logits, k=10), {0, 1, 2, 3})
        with self.assertRaises(ValueError):
            solver.top_k_sample(torch.tensor([]), k=1)
        with self.assertRaises(ValueError):
            solver.top_k_sample(torch.tensor([[1.0, 2.0]]), k=1)
        with self.assertRaises(ValueError):
            solver.top_k_sample(logits, k=0)
        for temperature in (0, -1):
            with self.subTest(temperature=temperature):
                with self.assertRaises(ValueError):
                    solver.top_k_sample(logits, k=2, temperature=temperature)

    def test_two_sum(self):
        solver = self.solution("two_sum.py")
        self.assertEqual(solver.twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(solver.twoSum([3, 3], 6), [0, 1])

    def test_valid_anagram(self):
        solver = self.solution("valid_anagram.py")
        self.assertTrue(solver.isAnagram("anagram", "nagaram"))
        self.assertFalse(solver.isAnagram("rat", "car"))
        self.assertTrue(solver.isAnagram("", ""))

    def test_valid_palindrome(self):
        solver = self.solution("valid_palindrome.py")
        self.assertTrue(solver.isPalindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(solver.isPalindrome("race a car"))
        self.assertTrue(solver.isPalindrome(".,"))

    def test_valid_parentheses(self):
        solver = self.solution("valid_parentheses.py")
        self.assertTrue(solver.isValid("()[]{}"))
        self.assertTrue(solver.isValid("{[]}"))
        self.assertFalse(solver.isValid("(]"))
        self.assertFalse(solver.isValid("]"))
        self.assertFalse(solver.isValid("("))

    @staticmethod
    def list_values(head):
        values = []
        while head is not None:
            values.append(head.val)
            head = head.next
        return values


if __name__ == "__main__":
    unittest.main()
