def main(): 
    with open("books/frankenstein.txt") as f:
        content = f.read()
        words = len(content.split())
        dict = CountLetters(content)
        list = SortedLetters(dict)
        print(f"{words} was found in the text:")
        for element in list:
            if not element["name"].isalpha():
                continue
            print(f"{element['name']} character was found {element['number']} times")

def CountLetters(words):
    lettersCount = {}
    for word in words:
        lower = word.lower()
        if lower in lettersCount:
            lettersCount[lower] += 1
        else:
            lettersCount[lower] = 0
    return lettersCount

def sortOn(dict):
    return dict["name"]

def SortedLetters(allChar):
    sortedList = []
    for char in allChar:
        sortedList.append({"name": char, "number": allChar[char]})
    sortedList.sort(key=sortOn)
    return sortedList

main()