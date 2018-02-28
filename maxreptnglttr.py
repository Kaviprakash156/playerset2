n = 256
def repeatingletter(str):
    count = [0] * n
    max = -1
    c = ''
    for i in str:
        count[ord(i)]+=1;
 
    for i in str:
        if max < count[ord(i)]:
            max = count[ord(i)]
            c = i
 
    return c
str =input("Enter the stirng:\n")
print ("Maximum repeating letter is:\n " + repeatingletter(str))
