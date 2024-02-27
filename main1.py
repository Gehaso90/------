# def print_formatted_text():
#     text = "Don't compare yourself with anyone in this world…\nif you do so, you are insulting yourself."
#     author = "Bill Gates"
#     formatted_text = text + "\n" + author
#     print(formatted_text)



# def print_even_numbers(a, b):

#     if a > b:
#         a, b = b, a
#     for i in range(a, b + 1):
        
#         if i % 2 == 0:
#             print(i)

# print_even_numbers(5, 15)




def print_square(size, symbol, filled=False):
    
    for i in range(size):
       
        for j in range(size):
           
            if filled:
                
                print(symbol, end="")
            else:
                if i == 0 or j == 0 or i == size - 1 or j == size - 1:
                    print(symbol, end="")
                else:
                    print(" ", end="")
        
        print()

print_square(5, "*", True)
print_square(5, "@", False)