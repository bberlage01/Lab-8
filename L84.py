#Rosemary Hoffman and Bethany B
# index=0
# s="mind the gap!"
# while index<len(s) and s[index] !=" ":
#     index+=1
# print(s[:index])
# def until_dot(x):
#     index=0
#     while index<len(x) and x[index] !=".":
#         index+=1
#     print(x[:index])
#
# until_dot("hello world. hello")
def find_512():
    for x in range(100):
        for y in range(100):
            if x*y==512:
                print("here")
                break
