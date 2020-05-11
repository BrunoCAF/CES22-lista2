import re

def cleanword(word):
    x = re.findall(pattern='\w', string=word)
    cleaned_word = ""
    for a in x: cleaned_word += a
    return cleaned_word

def has_dashdash(word):
    return (re.search(pattern="--", string=word) != None)

def extract_words(phrase):
    words = re.split(pattern='\W', string=phrase.lower())
    while '' in words: words.remove('')
    return words

def wordcount(word, word_list):
    return sum((1 if w == word else 0) for w in word_list)

def wordset(word_list):
    set_of_words = list(set(word_list))
    set_of_words.sort()
    return set_of_words

def longestword(word_list):
    return 0 if word_list == [] else max(len(w) for w in word_list)

assert(cleanword("what?") == "what")
assert(cleanword("'now!'") == "now")
assert(cleanword("?+='w-o-r-d!,@$()'") ==  "word")

assert(has_dashdash("distance--but"))
assert(not has_dashdash("several"))
assert(has_dashdash("spoke--"))
assert(has_dashdash("distance--but"))
assert(not has_dashdash("-yo-yo-"))

assert(extract_words("Now is the time!  'Now', is the time? Yes, now.") ==
      ['now','is','the','time','now','is','the','time','yes','now'])
assert(extract_words("she tried to curtsey as she spoke--fancy") ==
      ['she','tried','to','curtsey','as','she','spoke','fancy'])

assert(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
assert(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
assert(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
assert(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)

assert(wordset(["now", "is", "time", "is", "now", "is", "is"]) ==
      ["is", "now", "time"])
assert(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) ==
      ["I", "a", "am", "is"])
assert(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) ==
      ["a", "am", "are", "be", "but", "is", "or"])

assert(longestword(["a", "apple", "pear", "grape"]) == 5)
assert(longestword(["a", "am", "I", "be"]) == 2)
assert(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
assert(longestword([ ]) == 0)