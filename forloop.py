names = ["Helen", "Grace", "Favour", "David", "John"]
scores = (12,13,78,67,44,56,57,34,58,90)
total = 0

#printing each name in the names list
for name in names:
    print(name)

#getting the average of scores in the scores tuple    
for score in scores:
    total+=score    
avg = total/len(scores)
print("The Average of scores is =",avg)

# printing the even numbers in a tuple
for score in scores:
    if score%2 == 0:
        print(score)
        
        
# using range in a for loop
r = range(10)
print(r)
print(list(r))

for num in r:
    print(num)

#running a block of code for a specified number of times
for num in range(1,21):
    result = 12 * num
    print("12 X ", num, "=", result)
    
#iterating through a list using the range
for num in range(len(names)):
    print(names[num], "is at index", num)





