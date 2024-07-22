word = input()

length = len(word)

if length > 10:
    # first letter
    print(f"{word[0]}{length-2}{word[-1]} " )   
else:
    print(word)