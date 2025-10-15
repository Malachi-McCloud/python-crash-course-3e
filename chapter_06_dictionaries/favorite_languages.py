# Favorite Languages
# This starts our looping through dictionaries

# Create a disctionary of names with their favvorite languages
favorite_languages = {
    'Jen' : 'Python',
    'Sarah' : 'C',
    'Edward' : 'Rust',
    'Phil' : 'Python'
}

# Just to remember these can be called the same as any other variable in strings
# These are the same as a map in Java
for name in favorite_languages.keys():
    print(name.title())
for language in favorite_languages.values():
    print(language.title())
