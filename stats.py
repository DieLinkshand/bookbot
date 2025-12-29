def get_num_words(content):
	content = content.split()
	return len(content)

def get_num_characters(content):
    char_dict = {}
    
    for i in content.lower():
        if i not in char_dict:
            char_dict[i] = 1
        else:
            char_dict[i] += 1
    
    return char_dict

def create_report(num_of_chars):
    list_of_dicts = []
    for i in num_of_chars:
        list_of_dicts.append({"char": i, "num": num_of_chars[i]})
    list_of_dicts.sort(key=lambda x: x["num"], reverse=True)
    return list_of_dicts
