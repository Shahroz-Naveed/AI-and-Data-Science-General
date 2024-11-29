# 6. Write a function to count the vowels in a given string.
def vowel_count(string):
    vowels = "aeiouAEIOU"
    count = len([char for char in string if char in vowels])
    print(f"Number of vowels in string",count)
str = "Shahroz"
vowel_count(str)