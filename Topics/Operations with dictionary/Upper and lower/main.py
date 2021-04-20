# the list with words from string
# please, do not modify it
some_iterable = input().split()

result = {elem.upper(): elem.lower() for elem in some_iterable}

print(result)
