word= input("Введіть слово")
name = word[::-1]
print(*reversed(name.split()))