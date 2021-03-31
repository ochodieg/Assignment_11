# def get_books(filename: str)->list:
#     try:
#         fileref = open(filename,'r')
#         # fileref.close()
#
#         for line in fileref:
#
#             data = line.strip()
#
#
#
#
#     return fileref
#
# print(get_books("books.tsv"))
#
#

# fileref = open("books.tsv", "r")
# for line in fileref:
#     gay = line.split()
#     print(gay)


# fileref = open("books.tsv",'r')
# print(fileref.readlines())
def sortby_title(elem):
    """key that ensures tuple sorting
     by the title item"""
    return elem[0]

def sortby_isbn(elem):
    """key that allows tuple sorting
     by the ISBN item"""
    return elem[1]

def sortby_author(elem):
    """key that allows tuple sorting
     by the author name item"""
    return elem[2]

def sortby_price(elem):
    """key that allows tuple sorting
     by the price item"""
    return elem[3]




def check_file_name(name:str)-> str:
    clean_name = name.strip()
    # valid = True
    # while valid:
    for chk in [".txt", ".csv", ".tsv"]:
        filename = clean_name + chk
        if get_book_lst(filename) == []:
            valid = True
            returnval = "File not found."
        else:
            valid = False
            returnval = filename # parse_file.get_book_lst(filename)
    return returnval


def get_book_lst(str):
    book_list = []

    try:
        with open(str, "r") as file_list:
            lines = file_list.readlines()[1:]
            for line in lines:
                data = line.strip()
                parts = data.split("\t")
                title = parts[0]
                isbn = parts[1]
                authors = parts[2]
                price = float(parts[3])
                book_data = [title, isbn, authors, price]
                book_list.append(book_data)
    except Exception as err:
            # print(err)
            book_list = []
    return book_list


def get_books(filename: str) -> list:
    """accepts string as relative path to a file and returns
    a list of tuples with file information"""
    list_of_tuples = []
    try:
        with open(filename, "r") as file:
            # with statement takes automates closing the file
            # when no longer in use
            lines = file.readlines()[1:]
            # this slices the file. "readlines()" is used to parse
            # subsequent lines. However, in here, we give it the
            # index [1:] meaning, we parse through every file line
            # starting at line 1, not line 0. Then, every file-line
            # is parsed into the variable "lines"
            for line in lines:
                # this for loop uses the lines variable to iterate through
                # before the loop, each line is an item in a list where all
                # the 'tab' and 'new line' methods are still present.
                # every loop...

                data = line.strip()
                # .strip() method removes any unnecessary characters like white
                # space and the "\n' character
                parts = data.split("\t")
                # .split() method is used to split the items in the list.
                # so instead of every list item consisting of every file line,
                # now every list item will be separated by the delimiter "\t"
                # starting every line.
                title = parts[0]
                isbn = parts[1]
                authors = parts[2]
                price = float(parts[3])
                # these 4 variables will determine which indices in the list
                # items will be used for the tuples
                book_data = (title, isbn, authors, price)
                # this will be what the tuples consist of
                list_of_tuples.append(book_data)
                # this appends tuple items to our initial empty list

    except FileNotFoundError:
        print("did not find that file")
    except Exception as err:
        print("There was an error (" + str(err) + ") finding that file.")

    return list_of_tuples


def get_average_price(book_list: list) -> float:
    """accepts list of books and determines
    the average price for all the items in that list"""

    divisor = 0
    accumulated = 0
    try:
        for itm in book_list:
            accumulated += itm[3]
            # counts the 'itm' every iteration and sums their
            # float values for every iteration
            divisor += 1
            # an accumulator to keep track of how many 'itm' variables
            # are iterated. The sum is used as the divisor to calculate
            # the average
            # print(itm)
        avrg = accumulated/divisor
        avrg_2_deci = float("{:.2f}".format(avrg))

    except ZeroDivisionError:
        avrg_2_deci = "You can't divide by zero."
    except Exception as error:
        avrg_2_deci = "Looks like there was an error: " + str(error)
    return avrg_2_deci


def filter_by_title(book_list: list, search: str) -> list:
    """accepts a list of books and a str. It then uses the
    string as a search term and checks to see if the given string is found
    in one of the list items. Then those items that match are appended to new
    string"""
    # lowercase_search = search.lower()
    uppercase_search = search.upper()

    new_list = []
    # print(book_list)
    for itm in book_list:
        # lst = [x.upper() for x in book_list]

        tuple_item = itm[0]
        uppercase_item = tuple_item.upper()
        # itm2 = itm.isupper()
        if uppercase_search in uppercase_item:
            new_list.append(itm)
            # print(itm[0])
            # print(new_list)
    # if not new_list:
    #     new_list = "not found in title"
    new_list.sort(key=sortby_title)
    return new_list


def filter_by_isbn(book_list: list, search_trm: str) -> list:
    """accepts a list of books and a str. It then uses the
    string as a search term and checks to see if the given string is found
    in one of the list items. Then those items that match are appended to new
    string"""

    new_list = []
    for itm in book_list:
        if search_trm in itm[1]:
            new_list.append(itm)
    new_list.sort(key=sortby_isbn)

    return new_list


def filter_by_author(book_lst: list, search_trm: str) -> list:
    """accepts a list of books and a str. It then uses the
    string as a search term and checks to see if the given string is found
    in one of the list items. Then those items that match are appended to new
    string"""

    uppercase_search = search_trm.upper()
    new_list = []

    for itm in book_lst:
        # lst = [x.upper() for x in book_list]
        tuple_item = itm[2]
        uppercase_item = tuple_item.upper()
        # print(uppercase_item)
        # itm2 = itm.isupper()
        if uppercase_search in uppercase_item:
            new_list.append(itm)
            # print(itm[2])
            # print(new_list)
    new_list.sort(key=sortby_author)
    return new_list



def filter_by_price(book_lst: list,srch_price: float, maxmin: str) -> list:

    # maxval = True
    # minval = False
    maxmin_lowercase = maxmin.lower()
    # srch_str = str(srch_price)
    new_list = []

    if maxmin_lowercase == "x":
        # maxminval = maxval
        for itm in book_lst:
            tuple_item = itm[3]

            if srch_price >= tuple_item:
                new_list.append(itm)

    elif maxmin_lowercase == "n":
        # maxminval = minval
        for itm in book_lst:
            tuple_item = itm[3]

            if srch_price <= tuple_item:
                new_list.append(itm)
    #else:
        #maxminval = "Not a valid entry"
    # returnval = maxminval
    new_list.sort(key=sortby_price)
    return new_list



def get_table(tple_lst: list) -> str:
    """accepts list of tuples in format (int,int)
    and returns a string table with tuple information"""
    accumulator = 0 # keeps count of indices

    str_lst = ""
    total_price = 0

    # for loop iterates through indices instead of items
    for itm in tple_lst:

        accumulator += 1
        title = itm[0]
        # description calls get_generations and selects
        # a descriptor from that list. The iteration variable (itm)
        # is used to get an item from the tuple list, then the index
        # '1' is used to get an item from the tuple obtained
        ISBN = itm[1]
        # yrz gets an item from tuple list, using the iteration 'itm'
        # as the index and then gets an item from that tuple obtained
        # with index '0' then it is turned into a str type.
        author = itm[2]
        price = itm[3]
        withtax = price * 1.06
        accumulated = str(accumulator)
        # accumulator turns accumulator into string. this is just so that
        # it can be concatenated to the formatted string
        total_price += price

        usd = "$"

        str_lst += "{}\t{:<56}\t\t{:<16} {:<29}{:>4}{:.2f}\t\t${:.2f}\n".format(str(accumulated), title, ISBN, author, usd, price, withtax)
        # str_lst accumulated to a string for every iteration with new items



    proto_line = "I found {} results:\n".format(str(accumulator))
    first_line = "{}\t{:<61}\t{:<12}\t {}  {:>21}\t\t{}".format("#", "Book title", "ISBN", "Author Name(s)", "Price","w/tax")
    second_line = "======================================================================================================================================"
    third_line = str_lst
    fourth_line = "--------------------------------------------------------------------------------------------------------------------------------------"

    try:
        average_price = total_price/accumulator
        fifth_line = "{:>102}Average price: ${:.2f}".format("", average_price)
    except Exception as err:
        fifth_line = "{:>83}{}: Average price: $--.--".format("", str(err))

    table = "{}\n{}\n{}\n{}\n{}\n{}".format(proto_line, first_line, second_line, third_line, fourth_line, fifth_line)

    return table

