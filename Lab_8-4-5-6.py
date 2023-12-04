#Create a Python file named lab_8-4.py

#*** You must write a comment for every chunk of code you write from now on along with your author tag***

#Write a function count_a(word) that takes in a string word and returns the number of a's in the word. 
#The function should count both lowercase (a) and uppercase (A)
def count_a(word):
    r = 0
    for a in word:
        r += 1 if a == "a" or a == "A" else 0
    return r    
print(count_a("aaaaaAAAAAA"))
print(count_a("AAAhgfdxcvbhytrdcvbhnytrda"))
print(count_a("word"))
#_____________________________________________________________________________________

#Create a Python file named lab_8-5.py

#Write a function factorial(num) that takes in a number num 
#and returns the product of all numbers from 1 up to and including num
def factorial(num):
    r = 1
    for a in range(1,num+1):
        r = r * a
    return r    

print(factorial(3))
print(factorial(6))
print(factorial(4))  

#_______________________________________________________________________________________

#Create a Python file named lab_8-6.py

#Write a function is_palindrome(word) that takes in a string word 
#and returns the true if the word is a palindrome, false otherwise. 
def is_palindrome(word):
    list = []
    for a in word:
        list += a
    list.reverse()
    return word == "".join(list)
        
print(is_palindrome("tacocat"))
print(is_palindrome("sean"))
print(is_palindrome("bob"))
#A palindrome is a word that is spelled the same forwards and backwards.

