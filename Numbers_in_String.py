s=input()
add=0
for character in s:
    if character.isdigit():
        add=add+int(character)
print(add)