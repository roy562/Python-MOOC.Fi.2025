# Write your solution here
def new_person(name: str, age: int):
    
    if name == "":
        raise ValueError("Name is an empty string")
    elif len(name) > 40:
        raise ValueError("Name is longer than 40 characters: " + name)
    else:
        parts = name.split(" ")
        if len(parts) < 2:
            raise ValueError("Name is shorter than two words: " + name)
    
    
    if age < 0 :
        raise ValueError(f"Age: {age} cannot be negative")
    elif age > 150:
        raise ValueError("Age: %i cannot be greater than %i"%(age,150))

    return(name, age)


#new_person("Lalit Agrawal",32)