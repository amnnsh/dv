a=input("Enter the string: ")
vowel=0
c=0
a=a.lower()
for i in a:
    if i in ['a','i','o','e','u']:
        vowel+=1
    elif i!=' ':
        c+=1
print(f"Vowels are {vowel}")
print(f"Consonants are {c}")