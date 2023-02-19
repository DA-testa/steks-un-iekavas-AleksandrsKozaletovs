# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))

        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char,next):
                return i+1           
            opening_brackets_stack.pop()   
        if next.isnumeric():
            opening_brackets_stack.append(Bracket(next, i+1))
            return i+1
        if i == len(text)-1 and len(opening_brackets_stack) == 0: 
          return "Success" 
      

def main():
    text = input()
    if "I" in text:
        i = input()          
        mismatch = find_mismatch(i)
    elif "F" in text:
        openFilename = input()
        file = open(openFilename,"r")
        result = find_mismatch(file)
        print(result)
    else:
        mismatch = find_mismatch(text)
        print(mismatch)
         


if __name__ == "__main__":
    main()
