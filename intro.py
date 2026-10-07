text=" welcome to IMCC!   "

#Strip spaces from both ends
print("Remove spaces",text.strip())

text=text.strip()
print("Capitlize First letter",text.capitalize())

print(text.title())
# change the case
print(text.upper())
print(text.lower())

#count occurences of a substring  {can be  used for project}
print("Letter C occurs ",text.count("C"),"times in text")

# position of substring
print("Position of a IMCC in text",text.find("IMCC"))

#replace
print(text.replace("IMCC","Python Magic"))

# check if string starts or ends with certain substring
print(text.startswith(" we"))
print(text.endswith("  "))

#split
print("simple split",text.split())

#join
words=["Python","is","sus"]
print(" ".join(words))