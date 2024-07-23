# how many times you'll take the input from the user
n = int(input()) 

# loop for taking the input from the user
for _ in range(n):  
    word = input()  
    length = len(word)
    
    if length > 10:  
        print(f"{word[0]}{length-2}{word[-1]}")
    else:  
        print(word)