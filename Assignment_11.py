import parse_file

cunt = input("What is the name of the file? (dont include the extension) ")
file_check = parse_file.check_file_name(cunt)

validate = True
while validate:
    if file_check == "File not found.":
        print(file_check)
        cunt = input("What is the name of the file? (dont include the extension)")
        file_check = parse_file.check_file_name(cunt)
    else:
        file = file_check
        validate = False




# peepee = "books.tsv"
tuples = parse_file.get_books(file)
# print(poop)
# print("-1-1-1-1-1-1-1-1-1-1")
#
#
# print(parse_file.get_average_price(poop))
# print("-2-2-2-2-2-2-2-2-2-2-")
#
# # print("a".upper())
# # print("-3-3-3-3-3-3-3-3-3-3-3-3")
#
# # piss = parse_file.get_book_lst(peepee)
# # print(piss)
# # print("4-4-4-4-4-4-4-4-4-4-4-4-4-4-")
# print(parse_file.filter_by_title(poop, "comp"))
# print("-5-5-5-5-5-5-5-5-5-5-5-5-5-5-5")
# print(parse_file.filter_by_title(poop,"ml"))
# print("-5-5-5-5-5-5-5-5-5-5-5-5-5-5-")
#
# print(parse_file.filter_by_isbn(poop, "978-0135957059"))
# print("-6-6-6-6-6-6-6-6-6-6-6-6-6-6-6-")
# print(parse_file.filter_by_author(poop, "co"))
# print("7-7-7-7-7-7-7-7-7-7-7-7-7-7-7-7-7-")
# print(parse_file.filter_by_price(poop,1,"min"))
#
#
#
validated = True

while validated:
    options = input("\nFile was found.\nWhat would you like to filter and sort by?:\n"
                    "{}\n{}\n{}\n{}\n{}\nor get {}\n> "
    .format("(t)itle","(i)sbn","(a)uthor","ma(x) price","mi(n) price","a(l)l"))
    option_case = options.lower()

    if option_case == "title" or option_case == "t":
        notall = input("Search in title: ")
        variable = parse_file.filter_by_title(tuples, notall)
        print(parse_file.get_table(variable))
        # print(variable)
        validated = False

    elif option_case == "isbn" or option_case == "i":
        notall = input("Type in part of or the whole ISBN: ")
        variable = parse_file.filter_by_isbn(tuples, notall)
        print(parse_file.get_table(variable))
        # print(variable)
        validated = False

    elif option_case == "author names" or option_case == "a":
        notall = input("What is part of the author's name?: ")
        variable = parse_file.filter_by_author(tuples, notall)
        print(parse_file.get_table(variable))
        validated = False

    elif option_case == "max price" or option_case == "x":
        notall = input("What is the maximum price?: ")
        notall_float = float(notall)
        variable = parse_file.filter_by_price(tuples, notall_float,"x")
        print(parse_file.get_table(variable))
        validated = False

    elif option_case == "min price" or option_case == "n":
        notall = input("What is the minimum price?: ")
        notall_float = float(notall)
        variable = parse_file.filter_by_price(tuples, notall_float,"n")
        print(parse_file.get_table(variable))
        # print(variable)
        validated = False

    elif option_case == "list all" or option_case == "l":
        print("you chose list all")
        variable = tuples
        print(parse_file.get_table(tuples))
        validated = False

    else:
        print("\n!! INVALID CHOICE !!")
        validated = True

