"""
Sliding Window Pattern — Fixed Window Size k

Use when: You need to process every contiguous subarray (or substring) of fixed length k.
Idea: Maintain a window [left, right] of size k. Slide by moving right, then shrink from
      left when window size exceeds k. Update the answer when window size equals k.
"""


def sliding_window_fixed_k(nums, k):
    """
    Template for sliding window with window size exactly k.

    - Expand: add element at `right`.
    - Shrink: when window size > k, remove element at `left` and move left.
    - Process: when window size == k, update your answer (sum, max, etc.).
    """
    left = 0
    # answer = ...  # e.g. 0 for max sum, float('-inf') for max, etc.

    for right in range(len(nums)):
        # 1. Expand: include nums[right] in the window
        # ... update window state (e.g. add to running sum, update freq, etc.)

        # 2. Shrink: keep window size <= k
        while right - left + 1 > k:
            # Remove nums[left] from window state
            # ... update state (e.g. subtract from sum, decrement freq, etc.)
            left += 1

        # 3. When window size is exactly k, update answer
        if right - left + 1 == k:
            # ... compute and update answer (e.g. max sum, min, count, etc.)
            pass

    # return answer


# --- Example: Maximum sum of subarray of size k ---
def max_sum_subarray_of_size_k(nums, k):
    """Return the maximum sum of any contiguous subarray of length k."""
    left = 0
    window_sum = 0
    max_sum = float("-inf")

    for right in range(len(nums)):
        window_sum += nums[right]

        if right - left + 1 > k:
            window_sum -= nums[left]
            left += 1

        if right - left + 1 == k:
            max_sum = max(max_sum, window_sum)

    return max_sum if max_sum != float("-inf") else 0


if __name__ == "__main__":
    nums = [2, 1, 5, 1, 3, 2]
    k = 3
    print(f"Array: {nums}, k = {k}")
    print(f"Max sum of subarray of size {k}: {max_sum_subarray_of_size_k(nums, k)}")  # 9
