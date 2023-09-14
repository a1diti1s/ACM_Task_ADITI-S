def sum_odd_elements():
    sum=0
    t=int(input())
    list=[]
    for i in range(t):
        numbers=int(input())
        list.append(numbers)
    for n in list:
        if n%2!=0:
            sum+=n
    print(sum)
sum_odd_elements()