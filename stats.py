def num_words_in_book(str_book):
    new_book=str_book.split()
    return len(new_book)

def occurence_characters(str_book):
    book=str_book.lower()
    dictionnary={}
    for char in book:
        try:
            dictionnary[char]+=1
        except KeyError:
            dictionnary[char]=1
    return dictionnary

def sort(items):
    dictionnary_list=[]
    for key in items:
        dictionnary_list.append({"char": f"{key}","num": items[key] }) #ou créer 2 listes dict.keys() et dict.values() et append ({key: value})
    dictionnary_list.sort(reverse=True, key=help_sort_on)
    return dictionnary_list


    
    


def help_sort_on(item):
    return item["num"]


            