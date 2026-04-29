# a={1,2,3,6}
# print(a)
# it does not allow duplicates
uber_cites1=set(["chennai","bangalore","delhi","bangalore"])
uber_cites2={"chennai","bangalore","hyderabad","coorg"}

print(uber_cites1.union(uber_cites2))
print(uber_cites1.intersection(uber_cites2))
print(uber_cites2.difference(uber_cites1))

uber_cites1.add("salem")
print(uber_cites1)

uber_cites1.remove("delhi")
print(uber_cites1)

my_set={1,2,3,4,5}
print(my_set)
my_set.remove(5)
print(my_set)


# if there no values in the set,but we are removing...so,it should be safe
my_set.discard(8)
print(my_set)