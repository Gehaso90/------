# import json

# def load_unwanted_words(filename):
#     if os.path.exists(filename):
#         with open(filename, 'r') as file:
#             unwanted_words = set(json.load(file))
#         return unwanted_words
#     else:
#         return set()

# def remove_unwanted_words(text, unwanted_words):
#     words = text.split()
#     clean_words = [word for word in words if word not in unwanted_words]
#     return ' '.join(clean_words)

# def write_clean_text(filename, cleaned_text):
#     with open(filename, 'w') as file:
#         file.write(cleaned_text)

# unwanted_words = load_unwanted_words('unwanted_words.json')

# with open('text_file.txt', 'r') as file:
#     text = file.read()

# cleaned_text = remove_unwanted_words(text, unwanted_words)

# write_clean_text('clean_text_file.txt', cleaned_text)




















