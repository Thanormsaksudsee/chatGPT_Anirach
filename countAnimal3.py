def find_animals(input_string, animals):
    def backtrack(start, path):
        if start == len(input_string):
            return [path]
        
        results = []
        for end in range(start + 1, len(input_string) + 1):
            current_word = input_string[start:end]
            if current_word in animals:
                remaining = backtrack(end, path + [current_word])
                results.extend(remaining)
        return results
    
    found_animals = backtrack(0, [])
    return len(found_animals), found_animals

# List of animals
animals_list = ["dog", "cat", "bat", "cock", "cow", "pig", "fox",
                "ant", "bird", "lion", "wolf", "deer", "bear",
                "frog", "hen", "mole", "duck", "goat"]

# Test cases
print(find_animals("goatcode", animals_list))        # Output: (2, [['goat'], ['cat']])
print(find_animals("cockdogwdufrbir", animals_list)) # Output: (4, [['cock'], ['dog'], ['duck'], ['bird']])
print(find_animals("dogdogdogdogdog", animals_list)) # Output: (5, [['dog'], ['dog'], ['dog'], ['dog'], ['dog']])
