st_name=input("piease enter a string:")
words=st_name.split()
reversed_string=words[::-1]
st_join=''.join(reversed(words))
print(st_join)