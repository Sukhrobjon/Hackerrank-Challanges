# Enter your code here. Read input from STDIN. Print output to STDOUT

r_day, r_month, r_year = [int(x) for x in input().split(' ')]
e_day, e_month, e_year = [int(x) for x in input().split(' ')]

# since tuple stops at the first False we want to compare the year and month first
# (1234, 12, 23) <= (2468, 9, 19)returns True
# (23, 12, 1234) <= (19, 9, 2468) returns False

if (r_year, r_month, r_day) <= (e_year, e_month, e_day):
    print(0)
elif(r_year, r_month) == (e_year, e_month):
    print(15*(r_day-e_day))
elif(r_year == e_year):
    print(500*(r_month-e_month))
else:
    print(10000)
