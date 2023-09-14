def sum_of_odd_elements(arr):
    odd_sum=0
    for n in arr:
        if n%2!=0:
            odd_sum+=n
    return odd_sum
numbers=list(range(0,8))
result = sum_of_odd_elements(numbers)
print(result)