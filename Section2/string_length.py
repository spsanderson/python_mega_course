def string_length(mystring):
    if type(mystring) == int:
        return "Sorry, integers have no length"
    else:
        return len(mystring)

print(string_length("Steve"))    