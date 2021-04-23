import json

data = json.load(open("dictionary.json"))

def translate(w):
	w = w.lower()
	if w in data:
		return data[w]
	else:
		return "The word doesn't exist. Please double check it."

proceed = "y"
while proceed == "y":

	word = input("Enter word: ")
	output = translate(word)
	if type(output) == list:
		for item in output:
			print(item)
	else:
		print(output)
	proceed = input("continue?[y/n] : ")
	