#Rosemary H and Bethany B
#C
def count_character(word, target):
    total=0
    index=0
    while index<len(word):
        if word[index:index+len(target)]==target:
            total+=1
            index+=len(target)
        else:
            index+=1
    return total

print(count_character("bonbonbon","o"))
