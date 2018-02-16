"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard
Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.


"""


def findWords(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    R1=set("QWERTYUIOP")
    R2=set("ASDFGHJKL")
    R3=set("ZXCVBNM")
    final_words=[]
    for elem in words:
        w=set(elem.upper())
        if w.issubset(R1) or w.issubset(R2) or w.issubset(R3):
            final_words.append(elem)

    return final_words

if __name__=="__main__":

    words = ["Hello", "Alaska", "Dad", "Peace"]
    result = findWords(words)
    print(result)