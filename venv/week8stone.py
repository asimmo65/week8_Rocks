#Allen Simmons

#read N and Q
#Given the number of stones she collects each day
#N = numbers of days
#starting from the very first day

#Given Q = Queries
# In each Q provide N (number of days) to collect M = number of stones
#For the input
    # the first line contains N and Q (number of days and query)
    # the second line contains N (number of days) as integers,
    # which the ith integer denotes the number of stones she has collected ith day
    # the third line contians Q space-seperated integers,
    #M, where ith M denotes the ith query. ie, number of


from bisect import bisect_left as bisect_left
from itertools import accumulate as accumulate



days_and_querries = input()
stones = input()
querries = input()



n, q = days_and_querries.split()
stones_list = map(int,stones.split())
querries_list = map(int,querries.split())
stones_sum = list(accumulate(stones_list))



for i in querries_list:
count = bisect_left(stones_sum,i)+1
print(count)