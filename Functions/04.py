# 4. Write a function that takes a string and returns it reversed.
def string_revers(string):
    reverse = string[::-1]
    print("Reverse of entered string is : ", reverse)
s = input("Enter a string : ")
string_revers(s)