def camel_case(s): 
    return len([i for i in s if i.isupper()]) + 1

s = "saveChangesInTheEditor"
print(camel_case(s))
