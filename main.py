# main.py
import json
import sys
import pprint

class BookVaultManager():
    def __init__(self):
        pass

    def add_book(self, request):
        # print()
        prop_list = request.split("/")
        with open('./books_storage.json', 'r') as my_json_file:
            try:
                data = json.load(my_json_file)
                books_numb = len(data)+1
            except json.decoder.JSONDecodeError:
                books_numb = 1
                data = {}
            book_id = f"{books_numb:06}"
            while book_id in data.keys():
                books_numb += 1
                book_id = f"{books_numb:06}"
        book_properties ={"title":prop_list[0],
                        "author": prop_list[1],
                        "year": prop_list[2],
                        "status": "Available"
                        }
        description = {book_id: book_properties}
        data.update(description)
        with open('./books_storage.json', 'w') as my_json_file:
            json.dump(data, my_json_file, indent=2)
        pass

    def delete_book(self, request, sarching_mthod):
        book_id = BookVaultManager.search_book(self, request, sarching_mthod)
        #print(type(book_id))
        with open('./books_storage.json', 'r') as my_json_file:
            try:
                data = json.load(my_json_file)
                data.pop(book_id)
            except json.decoder.JSONDecodeError:
                print("Book Vault is empty")
        with open('./books_storage.json', 'w') as my_json_file:
            json.dump(data, my_json_file, indent=2)
        pass

    def search_book(self, request, sarching_mthod):
        with open('./books_storage.json', 'r') as my_json_file:
            data = json.load(my_json_file)
            # try:
            if sarching_mthod == '1':
                if data.get(request):
                    print(f"{data.get(request)} found")
                    book_id = request
                    #print(f'book_id: {book_id}')
                else:
                    print(f'Not found: {request}')
            elif sarching_mthod == '2':
                for id_of_dict, prop_dict in data.items():
                    if request == prop_dict['title']:
                        print(f"{prop_dict} found")
                        book_id = id_of_dict
                    else:
                        print(f'Not found: {request}')
            elif sarching_mthod == '3':
                for id_of_dict, prop_dict in data.items():
                    if request == prop_dict['author']:
                        print(f"{prop_dict} found")
                        book_id = id_of_dict
                    else:
                        print(f'Not found: {request}')
            elif sarching_mthod == '4':
                for id_of_dict, prop_dict in data.items():
                    if request == prop_dict['year']:
                        print(f"{prop_dict} found")
                        book_id = id_of_dict
                    else:
                        print(f'Not found: {request}')
        return book_id
            
    def show_all(self):
        with open('./books_storage.json', 'r') as my_json_file:
            data = json.load(my_json_file)
            for key, value in data.items():
                pprint.pprint(f"ID:{key}, {value}")

    def change_status(self, request, status):
        with open('./books_storage.json', 'r') as my_json_file:
            data = json.load(my_json_file)
            book_dict = data.get(request)
            if status == "0": 
                status_txt = "Issued" 
            else: 
                status_txt = "Available"
            if book_dict:
                book_dict['status'] = status_txt
                print(f"status of {data.get(request)} has been changed to '{status_txt}'")

        with open('./books_storage.json', 'w') as my_json_file:
            json.dump(data, my_json_file, indent=2)

    def helpme(self):
        with open("./readme.md", "r") as instructions:
            print(instructions.read())

"Now type the request. Example: Nineteen Eighty-Four/George Orwell/1949"

if __name__ == "__main__":
    # print("Welcome to Book Vault! Write 'helpme' to see all utilities that you can use")

    book_manager = BookVaultManager()
    print("Welcome to Book Vault!Write 'helpme' to see all utilities that you can use")
    
    while True:
        starter_input = input("Make your command:")
        if starter_input == 'helpme':
            starter_input = book_manager.helpme()

        #request = input("Book's name, author and year are needed. Please, enter at least one of them:")

        if starter_input == 'add the book' or starter_input =='add':
            request = input("Book's name, author and year are needed. Please, enter as follows: Name/Author/year")
            book_manager.add_book(request)
            print("The book has been added successfully!")

        if starter_input == 'delete the book' or starter_input =='delete':
            sarching_mthod = input("""To delete the book you have to enter the name, author, year or id. 
                                   Please enter searching method: 
                                   1.by id 
                                   2.by name 
                                   3.by author 
                                   4.by year""")
            if sarching_mthod == '1':
                mthod_txt = 'id'
            elif sarching_mthod == '2':
                mthod_txt = 'name'
            elif sarching_mthod == '2':
                mthod_txt = 'author'
            elif sarching_mthod == '2':
                mthod_txt = 'year'
            request = input(f"enter {mthod_txt}:") 
            book_manager.search_book(request, sarching_mthod)
            book_manager.delete_book(request, sarching_mthod)
            print("The book has been deleted!")

        if starter_input == 'search':
            sarching_mthod = input("""To narrow the list of the books down please enter searching method: 
                                   1.by id 
                                   2.by name 
                                   3.by author 
                                   4.by year""")
            if sarching_mthod == '1':
                mthod_txt = 'id'
            elif sarching_mthod == '2':
                mthod_txt = 'name'
            elif sarching_mthod == '2':
                mthod_txt = 'author'
            elif sarching_mthod == '2':
                mthod_txt = 'year'
            request = input(f"enter {mthod_txt}:") 
            book_manager.search_book(request, sarching_mthod)

        if starter_input == 'change the status' or starter_input =='status':
            request = input("Book's id is needed. Please, enter:")
            status = input("To align the status to the book you have to enter 0 or 1, where 0 - Issued, 1 - Available:")
            book_manager.change_status(request, status)

        
        if starter_input == 'stop':
            print('session is stopping...')
            break

        if starter_input == 'showall':
            book_manager.show_all()

