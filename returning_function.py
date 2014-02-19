
def surround_with(surrounding):
    """ Return a function that takes a single argument and. """
    def surround_with_value(word):
        return '{}{}{}'.format(surrounding, word, surrounding)
    return surround_with_value

def transform_words(content, targets, transform):
    """Returns a string based on *content* but with each occurence of words 
    in *targets* replaced with the result of applying *transform* to it."""
    results = ''
    for word in content.split():
        if word in targets:
            results += ' {}'.format(transform(word))
        else:
            results +=  ' {}'.format(word)
    return results


markdown_string = 'My name is Rohit Khatana and I like Python but I do not own a Python'
markdown_string_italicized = transform_words(markdown_string, ['Python', 'Rohit'], surround_with('*'))

print markdown_string_italicized
