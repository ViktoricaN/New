def new_array(size=10, max=50):
    from random import randint
    return [randint(0, max) for _ in range(size)]

def merge_sort(x):

    if len(x) <= 1:
        return x

    middle = int(len(x) / 2)

    left, right = merge_sort(x[:middle]), merge_sort(x[middle:])

    return merge(left, right)


def merge(left, right):

    result = []
    left_pointer = right_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):

        if left[left_pointer] < right[right_pointer]:

            result.append(left[left_pointer])
            left_pointer += 1

        else:

            result.append(right[right_pointer])
            right_pointer += 1

    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])

    return result


array = new_array()
print(array)

result = merge_sort(array)
print(result)