"""
Sliding Window Pattern — Variable Window Size

Use when: You need longest/shortest contiguous subarray (or substring) satisfying a condition.
         e.g. "Longest subarray with sum <= S", "Minimum window containing all chars".
Idea: Expand right until condition is met; shrink left to improve (min/max length); track best.
"""


def sliding_window_variable(nums, condition_ok, update_best):
    """
    Template for sliding window with variable size.

    - Expand: add element at `right`, update window state.
    - Shrink: while window violates constraint, remove element at `left` and move left.
    - Process: when window is valid, update your answer (longest/shortest, etc.).

    condition_ok: function(window_state) -> bool
    update_best: function(best_so_far, left, right, window_state) -> new_best
    """
    left = 0
    # window_state = ...  # e.g. running sum, frequency map, etc.
    # best = ...  # e.g. 0 for max length, float('inf') for min length

    for right in range(len(nums)):
        # 1. Expand: include nums[right] in the window
        # ... update window_state (e.g. add to sum, update freq, etc.)

        # 2. Shrink: while window violates the constraint
        # while not condition_ok(window_state):
        #     ... remove nums[left] from window_state
        #     left += 1

        # 3. Window is now valid; update best (e.g. longest or shortest length)
        # best = update_best(best, left, right, window_state)
        pass

    # return best


# --- Example: Longest subarray with sum <= S (from arrays_patterns.md) ---
def longest_subarray_sum_at_most_s(nums, s):
    """
    Return the length of the longest contiguous subarray with sum <= s.
    Variable window: expand right, shrink left when sum > s, track max length when valid.
    """
    left = 0
    window_sum = 0
    max_length = 0

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum > s and left <= right:
            window_sum -= nums[left]
            left += 1

        # Window [left, right] has sum <= s
        max_length = max(max_length, right - left + 1)

    return max_length


if __name__ == "__main__":
    nums = [2, 1, 5, 1, 3, 2]
    s = 7
    print(f"Array: {nums}, s = {s}")
    print(
        f"Longest subarray with sum <= {s}: {longest_subarray_sum_at_most_s(nums, s)}"
    )  # 3 (e.g. [1, 5, 1] sum=7 or [1, 3, 2] sum=6, both length 3)
