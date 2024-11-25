class BubbleSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        n = len(self.arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]

    def get_sorted_array(self):
        return self.arr

# Usage
bs = BubbleSort([64, 34, 25, 12, 22, 11, 90])
bs.sort()
print("Bubble Sort:", bs.get_sorted_array())


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Usage
print("Insertion Sort:", insertion_sort([64, 34, 25, 12, 22, 11, 90]))








def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Usage
print("Selection Sort:", selection_sort([64, 34, 25, 12, 22, 11, 90]))







def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Usage
arr = [64, 34, 25, 12, 22, 11, 90]
merge_sort(arr)
print("Merge Sort:", arr)




def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Usage
print("Linear Search:", linear_search([64, 34, 25, 12, 22, 11, 90], 22))






def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Usage
sorted_arr = [11, 12, 22, 25, 34, 64, 90]
print("Binary Search:", binary_search(sorted_arr, 22))





class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

# Usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder Traversal:", end=" ")
inorder_traversal(root)
print()







