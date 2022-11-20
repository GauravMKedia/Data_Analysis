import re


# Function to Merge two string with unique characters
def merge_string(new_string1,new_string2):
    dict1={}
    dict2={}
    for i in new_string1:
        dict1[i] = dict1.get(i, 0) + 1
    for i in new_string2:
        dict2[i] = dict2.get(i,0) + 1;
    merged_string = ""
    for i in dict1:
        merged_string += i
    for i in dict2:
        merged_string += i
    return merged_string


# Function to check Anagram present between two set of strings
def CheckAnagram(s1, s2):
    arr=[]
    for i in s1:
        sorted_string=sorted(i)
        for j in s2:
            if sorted_string==sorted(j):
                new=(i)
                arr += i
    return arr

string1 ="OIUDFGHJK@UGPJH9876543JHG67LKJf56b,euqinu"
string2 = "PLKJ^&*@#$%PO*&kjhg&*,inuque,*5543gvdftyhgyu(&^&(*&^%6433lu"
f = open("Output.txt",'w')
f.write("Name     : Gaurav Kedia\nBranch   : CSE(AIML)\nSemester : 5\nCollege  : Shri Ramdeobaba College of Engineering and Management, Nagpur")
f.write("\n\n\nTask Description :\nRemove all numbers, special characters from two strings, split it, count the number of characters in strings.\nSub questions :\n1.Merge these two strings with unique characters\n2.After Merging replace H with 12345\n3.Split the strings check Anagram is there in the string or not.")
f.write("\n\nString1 = OIUDFGHJK@UGPJH9876543JHG67LKJf56b,euqinu \nString2 = PLKJ^&*@#$%PO*&kjhg&*,inuque,*5543gvdftyhgyu(&^&(*&^%6433lu\n")
f.write("\n\nOutput :\n")


# Removing Special Chaacter and Number from String
new_string1 = re.sub(r"[^a-zA-Z]","",string1)
new_string2 = re.sub(r"[^a-zA-Z]","",string2)
f.write(f"\nStrings after removal of special character and number is : \nString1={new_string1}\nString2={new_string2}\n")


# Length of String after removal of Special character and number
length1 = len(new_string1)
length2 = len(new_string2)
f.write(f"\nLength of String after removal of special character and number is :\nString1 = {length1}\nString2 = {length2}\n")


# Splitting String on Basis of Special Character and Number
split_string1 = re.sub(r"[^a-zA-Z]"," ",string1).split()
split_string2 = re.sub(r"[^a-zA-Z]"," ",string2).split()
f.write(f"\nString after doing split is :\nString1={split_string1}\nString2={split_string2}\n")

# Merging String with Unique Character
merged_string=merge_string(new_string1,new_string2)
f.write(f"\nString with unique character after merging is : {merged_string}\n")

# String after replacing H by 12345
f.write(f"\nInitial String = {merged_string}\nString after replacing H with 12345 is : {merged_string.replace('H','12345')}\n")

# Checking if there is Anagram present in strings fomrmed by splitting using special character and number
str_anagram = CheckAnagram(split_string1,split_string2)
listToStr = ' '.join([str(elem) for elem in str_anagram])
listToStr = listToStr.replace(" ","")
f.write(f"\nAnagram is :{listToStr}")

