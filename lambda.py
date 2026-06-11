from functools import reduce
# lambda argument:expression

# squ=lambda x :x*x
# print(squ(2))


# map
# map(function,iterable)
# fruits=['apple','banana','cherry']
# result=list(map(lambda fruit:fruit.upper(),fruits))
# print(result)
#
# # filter
# nums=[1,2,3,4,5,6,7,8,9,10]
# even=list(filter(lambda num:num%2==0,nums))
# print(even)
#
# # reduce
# nums=[1,2,3,4,5]
# total=reduce(lambda x,y:x+y,nums)
# print(total)


# max num
# nums=[10,5,3,7]
# max=reduce(lambda x,y:x if x>y else y,nums)
# print(max)



# real time example

prices=[250,900,1200,400,1500]
expensive=list(filter(lambda x:x>1000,prices)) #1200,1500
total= reduce(lambda a,b: a+b,expensive) #1200+1500=2700
print(total)