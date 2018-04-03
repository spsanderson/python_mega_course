def string_length(mystring):
    if type(mystring) == int:
        return "Sorry, integers have no length"
    elif type(mystring) == float:
        return "Sorry, floats have no length"
    else:
        return len(mystring)

print(string_length(1.1))    