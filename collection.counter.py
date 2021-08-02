from collections import Counter
shoe_no=int(input())
ip = list(map(int, input().strip().split()))[:shoe_no]
shoe_size=Counter(ip)
noofcust=int(input())
total=0
for i in range(noofcust):
    tmp=input()
    size,price=map(int,tmp.split())
    print(size,price)
    if size in shoe_size:
            if shoe_size[size]>0:
                total=total+price
                shoe_size[size]-=1
    else:
        pass
print(total)