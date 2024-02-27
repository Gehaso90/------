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




# def get_common_symbols(files):
#     common_symbols = set(files[0])
#     for file in files[1:]:
#         common_symbols &= set(file)
#     return common_symbols

# def read_files(file_names):
#     files = []
#     for file_name in file_names:
#         with open(file_name, 'r') as file:
#             files.append(file.read())
#     return files

# def write_common_symbols(common_symbols, output_file):
#     with open(output_file, 'w') as file:
#         for symbol in common_symbols:
#             file.write(symbol)

# def main():
#     file_names = []
#     while True:
#         file_name = input("Enter file name (or 'quit' to stop): ")
#         if file_name.lower() == 'quit':
#             break
#         file_names.append(file_name)

#     files = read_files(file_names)
#     common_symbols = get_common_symbols(files)
#     output_file = input("Enter output file name: ")
#     write_common_symbols(common_symbols, output_file)

# if __name__ == "__main__":
#     main()

















