# Array Patterns - Interview Prep Overview

A concise reference for array-based coding interview questions. Problems usually fall into a few **main patterns** and **sub-patterns**; recognizing which pattern fits is most of the work.

---

## Table of Contents

1. [Sliding Window](#1-sliding-window)
2. [Two Pointers](#2-two-pointers)
3. [Prefix Sum / Running Sum](#3-prefix-sum--running-sum)
4. [Binary Search on Array (or Answer)](#4-binary-search-on-array-or-answer)
5. [Kadane's Algorithm (Maximum Subarray)](#5-kadanes-algorithm-maximum-subarray)
6. [Dutch National Flag / Three-Way Partition](#6-dutch-national-flag--three-way-partition)
7. [Cyclic / Index Mapping (Array as Hash)](#7-cyclic--index-mapping-array-as-hash)
8. [Merge Intervals](#8-merge-intervals)
9. [Monotonic Stack / Queue](#9-monotonic-stack--queue)
10. [Quick Decision Guide](#quick-decision-guide)

---

## 1. Sliding Window

Maintain a contiguous window that expands or shrinks while tracking a condition (sum, count, etc.).

**When to use:** Keywords like *contiguous subarray/substring*, *fixed size k*, *longest/shortest*, *sum <= S*, *at most K distinct*, *minimum window containing*.

**Approach:** Expand right to include new element; shrink left when window violates the constraint (or when size > k); update the answer when the window is valid.

**Example problems:**

- Max sum subarray of size K
- Longest subarray with sum <= S
- Minimum window substring
- Longest substring with at most K distinct characters
- Max consecutive ones III
- Subarray product less than K
- Permutation in string

| Sub-pattern        | Use when                                                                 | Key idea                                                                 |
|--------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------|
| **Fixed size (k)** | "Max sum of subarray of size k", "Average of every k elements"          | Window length is always k. Expand right, shrink left when size > k; update when size == k. |
| **Variable size**  | "Longest subarray with sum <= S", "Minimum window containing all chars" | Expand right until condition is met; shrink left to improve (min/max length); track best. |
| **At most / at least k** | "Longest subarray with at most 2 distinct", "Subarrays with exactly k odd" | Combine fixed/variable logic with a condition (e.g. count distinct, count odd). |

> **Tip:** If the problem says "contiguous" and "subarray" or "substring", think sliding window first.

---

## 2. Two Pointers

Use two indices (same or opposite direction) to traverse the array and satisfy a condition without brute force.

**When to use:** *Sorted array*, *pair/triplet that sum to X*, *in-place*, *remove duplicates*, *move zeros*, *merge two sorted arrays*, *container with most water*.

**Approach:** Opposite ends: move left/right based on sum vs target; same direction: one pointer scans, one is the write position; two arrays: one pointer per array, advance the one that helps.

**Example problems:**

- Two sum II (sorted)
- Three sum
- Container with most water
- Remove duplicates in-place
- Move zeros
- Partition labels
- Merge two sorted arrays
- Intersection of two sorted arrays
- Trapping rain water

| Sub-pattern                 | Use when                                                                 | Key idea                                                                 |
|-----------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------|
| **Opposite ends**           | Sorted array, "two sum", "three sum", "container with most water"        | `left = 0`, `right = n-1`; move based on comparison with target.         |
| **Same direction (fast/slow)** | Remove duplicates in-place, move zeros, partition                    | One pointer scans, one points to "write position" or "next valid spot".  |
| **Two arrays**              | Merge two sorted arrays, intersection of sorted arrays                  | One pointer per array; advance the one that gives the smaller (or next) value. |

> **Tip:** "Sorted array" + "find pair/triplet" -> two pointers (or binary search). "In-place" + "reorder" -> same-direction two pointers.

---

## 3. Prefix Sum / Running Sum

Precompute cumulative sums so any range sum is O(1); combine with a hash map to count subarrays with a given sum.

**When to use:** *Subarray sum*, *range sum [i, j]*, *number of subarrays with sum K*, *continuous subarray sum*, *binary subarrays with sum*.

**Approach:** Build `prefix[i] = sum(nums[0..i])`; range `[i,j] = prefix[j] - prefix[i-1]`; for "count subarrays sum=K" store prefix-sum frequencies and at each j count `prefix[j] - K`.

**Example problems:**

- Subarray sum equals K
- Contiguous array (0s and 1s)
- Range sum query immutable
- Count subarrays with sum K
- Maximum size subarray sum equals K
- Find pivot index
- Product of array except self (concept)

| Sub-pattern                | Use when                                           | Key idea                                                                 |
|----------------------------|----------------------------------------------------|--------------------------------------------------------------------------|
| **1D prefix sum**          | Sum of range [i, j], count subarrays with sum = K  | `prefix[i] = sum(nums[0..i])`; range sum = `prefix[j] - prefix[i-1]`.    |
| **Prefix sum + hash map**  | "Number of subarrays with sum exactly K"           | Store frequency of prefix sums; for each `prefix[j]`, count how many `prefix[i]` with `prefix[j] - prefix[i] = K`. |
| **Prefix sum + min/max**   | "Max subarray sum", "Best time to buy/sell" (prefix view) | Track running sum and min prefix seen; max sum = current prefix - min prefix. |

> **Tip:** "Subarray sum" or "number of subarrays with sum K" -> prefix sum (often with a hash map).

---

## 4. Binary Search on Array (or Answer)

Halve the search space (index or possible answer) each step until you find the target or the min/max valid value.

**When to use:** *Sorted array*, *find target*, *first/last position*, *minimum/maximum X such that*, *rotated sorted*, *search in rotated array*.

**Approach:** Classic: `mid = (lo+hi)//2`, compare `arr[mid]` with target, narrow lo/hi; on answer: binary search on value range, define `check(mid)`, find smallest/largest valid mid; rotated: compare mid with ends to know which half is sorted.

**Example problems:**

- Binary search
- Find first and last position of element
- Search in rotated sorted array
- Find minimum in rotated sorted array
- Koko eating bananas
- Capacity to ship packages in D days
- Split array largest sum
- Search insert position

| Sub-pattern               | Use when                                                      | Key idea                                                                 |
|---------------------------|---------------------------------------------------------------|--------------------------------------------------------------------------|
| **Classic BS on index**   | "Find target in sorted array", "First/last position of element" | `mid = (lo+hi)//2`; move lo/hi by comparing `arr[mid]` with target; handle first/last with small logic change. |
| **Binary search on value (answer)** | "Koko eating bananas", "Minimum capacity to ship in D days" | Search space = possible answers; `check(mid)` = "can we achieve with value mid?"; find min/max valid. |
| **Rotated / modified sorted** | "Search in rotated sorted array", "Find minimum in rotated array" | Compare `arr[mid]` with `arr[lo]` or `arr[hi]` to see which half is sorted and where target can lie. |

> **Tip:** Sorted + search -> binary search. "Minimum X such that..." or "Maximum X such that..." -> often binary search on the answer.

---

## 5. Kadane's Algorithm (Maximum Subarray)

One pass: at each index, either extend the previous subarray or start fresh; track the best sum seen.

**When to use:** *Maximum sum contiguous subarray*, *largest sum*, *best time to buy and sell stock* (one transaction), *circular subarray*.

**Approach:** `cur = max(nums[i], cur + nums[i])`, `best = max(best, cur)`; for circular: answer = max(normal Kadane, total sum - min subarray sum).

**Example problems:**

- Maximum subarray
- Best time to buy and sell stock
- Maximum sum circular subarray
- Maximum product subarray (variant)
- Maximum sum of two non-overlapping subarrays

| Sub-pattern          | Use when                                                                 | Key idea                                                                 |
|----------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------|
| **Max subarray sum** | "Maximum sum subarray", "Best time to buy/sell stock (one transaction)" | `cur = max(nums[i], cur + nums[i])`, `best = max(best, cur)`.            |
| **Circular / wrap-around** | "Maximum sum circular subarray"                                   | Max of: (1) normal Kadane, (2) total sum - min subarray sum (invert signs and run Kadane). |

> **Tip:** "Largest sum contiguous subarray" (no fixed k) -> Kadane. If circular, combine Kadane with total/min subarray.

---

## 6. Dutch National Flag / Three-Way Partition

Partition the array into 2 or 3 regions in one pass using pointers that mark boundaries; swap elements into the correct region.

**When to use:** *Sort colors*, *0s 1s 2s*, *move all zeros*, *partition*, *in-place*, *O(n) one pass*, *few distinct values*.

**Approach:** Two-way: one pointer for next write position, scan and swap zeros (or evens) to front; three-way: lo, mid, hi; mid scans, swap with lo (0) or hi (2), advance lo/mid/hi accordingly.

**Example problems:**

- Sort colors (Dutch national flag)
- Move zeroes
- Sort array by parity
- Partition array according to pivot
- Wiggle sort II (concept)

| Sub-pattern           | Use when                                  | Key idea                                                                 |
|-----------------------|-------------------------------------------|--------------------------------------------------------------------------|
| **Two-way partition** | Move zeros to end, move evens before odds | Two pointers: one for "next write", one scanning; swap when condition met. |
| **Three-way (DNF)**   | Sort 0s, 1s, 2s; partition into three regions | `lo`, `mid`, `hi`; `mid` scans; swap with `lo` or `hi` based on value; adjust `lo`/`hi`/`mid`. |

> **Tip:** "Sort" or "partition" with only 2-3 values -> two/three-way partition.

---

## 7. Cyclic / Index Mapping (Array as Hash)

Use the array index as key: mark visited by negating or adding n; or place each value at index value-1 by swapping (cyclic sort).

**When to use:** *Elements in [1, n]* or *[0, n-1]*, *find duplicate*, *find missing*, *first missing positive*, *find all disappeared*, *O(1) space*.

**Approach:** Mark: for each x, negate `nums[x-1]` (or add n); rescan for positive = missing index; cyclic sort: swap `nums[i]` to index `nums[i]-1` until correct, then find first i where `nums[i] != i+1`.

**Example problems:**

- Find the duplicate number
- Find all numbers disappeared in array
- First missing positive
- Set mismatch
- Find duplicate in array (single duplicate)
- Cyclic sort (generic)

| Sub-pattern       | Use when                                               | Key idea                                                                 |
|-------------------|--------------------------------------------------------|--------------------------------------------------------------------------|
| **Index as key**  | "Find duplicate in [1,n]", "Find all numbers disappeared in array" | For each `x`, mark index `x-1` (e.g. negate or add n); re-scan to see which index was not touched. |
| **Cyclic sort**   | "Smallest missing positive", "Set mismatch"           | Put each value at index `value-1` by swapping; then iterate to find first `arr[i] != i+1`. |

> **Tip:** Values in [1, n] or [0, n-1] + find duplicate/missing -> think "array as hash" or cyclic sort.

---

## 8. Merge Intervals

Sort by start (or sweep all endpoints), then merge overlapping intervals or count overlaps in one pass.

**When to use:** *Intervals*, *merge overlapping*, *insert interval*, *minimum meeting rooms*, *non-overlapping*, *merge ranges*, *maximum overlapping*.

**Approach:** Sort by start; for each interval, if it overlaps the last in result then extend last, else append; for rooms: sort starts and ends, sweep and count +1/-1, track max; insert: find overlap range, merge into one, replace.

**Example problems:**

- Merge intervals
- Insert interval
- Meeting rooms II (min rooms)
- Non-overlapping intervals
- Interval list intersections
- Merge intervals (by start)
- Employee free time

| Sub-pattern     | Use when                         | Key idea                                                                 |
|-----------------|----------------------------------|--------------------------------------------------------------------------|
| **Sort + merge**| Merge overlapping intervals     | Sort by start; if current overlaps last in result, extend last; else append. |
| **Insert one**  | Insert new interval into sorted non-overlapping | Find overlap range; merge into one interval; replace overlapping with merged. |
| **Sweep line**  | "Minimum rooms", "Max overlapping" | Sort all starts and ends; sweep and count +1 / -1; track max count.   |

> **Tip:** "Intervals" + "merge" or "overlap" -> sort by start (or sweep line for counts).

---

## 9. Monotonic Stack / Queue

Stack (or deque) that keeps elements in sorted order; use to find next/previous greater or smaller in O(n), or window max.

**When to use:** *Next greater element*, *next smaller*, *daily temperatures*, *largest rectangle in histogram*, *sliding window maximum*, *previous greater*.

**Approach:** Stack: push indices; when current is greater than stack top, pop - that index's "next greater" is current; for window max use deque in decreasing order, front = max, remove from back when smaller.

**Example problems:**

- Next greater element I and II
- Daily temperatures
- Largest rectangle in histogram
- Trapping rain water (stack approach)
- Sliding window maximum
- Remove k digits
- Shortest unsorted continuous subarray (concept)

| Sub-pattern              | Use when                                      | Key idea                                                                 |
|--------------------------|-----------------------------------------------|--------------------------------------------------------------------------|
| **Next greater / smaller** | "Next greater element I/II", "Daily temperatures" | Stack holds indices; pop when current is greater (or smaller); popped index's "next" is current. |
| **Largest rectangle**    | "Largest rectangle in histogram"              | For each bar, find left/right boundaries (first smaller) using monotonic stack; area = height * width. |
| **Sliding window max/min** | "Max in every sliding window of size k"     | Deque maintaining indices in decreasing order of value; front = current window max. |

> **Tip:** "Next greater/smaller" or "previous greater/smaller" -> monotonic stack. "Max in sliding window" -> deque.

---

## Quick Decision Guide

| If the problem asks for... | Likely pattern |
|----------------------------|----------------|
| Contiguous subarray of **fixed length k** | Sliding window (fixed k) |
| **Longest/shortest** contiguous subarray satisfying condition | Sliding window (variable) |
| **Two/three elements** that sum to X (sorted array) | Two pointers |
| **Number of subarrays** with sum K | Prefix sum + hash map |
| **Maximum sum** of any subarray (no k) | Kadane |
| **Range sum** [i, j] or "subarray sum" | Prefix sum |
| Sorted array **search** or **first/last position** | Binary search |
| **Partition** 0s/1s/2s or few values | Dutch national flag |
| Values in [1,n], **duplicate/missing** | Cyclic sort / index as hash |
| **Intervals** merge/insert/overlap | Merge intervals |
| **Next greater/smaller** or **window max** | Monotonic stack/deque |

---

You can use this doc to map problem wording to a pattern, then implement using the right sub-pattern (e.g. the Sliding Window fixed-k template in `arrays/sliding_window_fixed_k.py`).
