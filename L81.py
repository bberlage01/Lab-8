#Rosemary Hoffman, Bethany Berlage
def total_length(x):
    sum=0
    for y in x:
        sum=len(y)+sum
    return sum
print(total_length(["hello","goodbye"]))


s="tenochtitlan"
index=0
while index<len(s):
    index+=1
    print(s[:index])
