import sys
from stats import get_num_words, get_num_characters, create_report

def get_book_text(filepath):
	with open(filepath) as file:
		content = file.read()
		return content

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		content = get_book_text(sys.argv[1])
		num_words = get_num_words(content)
		num_chars = get_num_characters(content)
		list_of_chars = create_report(num_chars)
		
		print("============ BOOKBOT ============")
		print("Analyzing book found at books/frankenstein.txt...")
		print("----------- Word Count ----------")
		print(f"Found {num_words} total words")
		print("--------- Character Count -------")
		for i in list_of_chars:
			if i['char'].isalpha():
				print(f"{i['char']}: {i['num']}")
			else:
				continue
		print("============= END ===============")



main()