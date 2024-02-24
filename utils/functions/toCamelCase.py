import re

def toCamelCase(inputString, capitalizeFirst=True):
    # Split the string into words using underscore, dash, or space
    words = re.split('[_\s-]', inputString)
    
    # # If there's only one word, return it directly
    if len(words) == 1:
        if capitalizeFirst:
            return words[0][:1].upper() + words[0][1:]
        else:
            return words[0]
    
    # Capitalize each word based on the capitalize_first parameter
    if capitalizeFirst:
        words = [word.capitalize() for word in words]
    else:
        words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
    
    # Join the words to form camelCase string
    camelCaseSring = ''.join(words)
    
    return camelCaseSring

