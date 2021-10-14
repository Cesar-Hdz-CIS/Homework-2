#Cesar Hernandez 1835494
init_word = input()
#print(init_word)
word = ""
reverse_word = ""

for i in init_word:
    if i != " ":
        word += i
        reverse_word = i + reverse_word
#print(reverse_word)
#print(word)
if word == reverse_word:
    print(init_word, "is a palindrome")
else:
    print(init_word, 'is not a palindrome')