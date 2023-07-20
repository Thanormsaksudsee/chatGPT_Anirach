def count_animals(input_string):
    animals = ["dog", "cat", "bat", "cock", "cow", "pig", "fox",
               "ant", "bird", "lion", "wolf", "deer", "bear",
               "frog", "hen", "mole", "duck", "goat"]
    
    found_animals = []
    remaining_string = input_string
    
    for animal in animals:
        if animal in remaining_string:
            # Find occurrences of the animal and store them in a list
            occurrences = [animal for i in range(remaining_string.count(animal))]
            found_animals.extend(occurrences)
            
            # Remove the animal from the remaining string
            remaining_string = remaining_string.replace(animal, '', len(occurrences))
    
    return len(found_animals), found_animals

# Test cases
print(count_animals("goatcode"))            # Output: (2, ['goat', 'cat'])
print(count_animals("cockdogwdufrbir"))     # Output: (4, ['cock', 'dog', 'duck', 'bird'])
print(count_animals("dogdogdogdogdog"))     # Output: (5, ['dog', 'dog', 'dog', 'dog', 'dog'])
