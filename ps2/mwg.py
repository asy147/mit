import string

wordlist = "app", "apple", "banana", "apt", "dota", "ample", "amply"

def match_with_gaps(my_word, other_word):
    my_word = "".join(my_word.split())
    if len(my_word) != len(other_word):
        return False
    else:
        for compare in zip(my_word,other_word):
            if compare[0] == "_":
                continue
            elif my_word.count(compare[0]) != other_word.count(compare[1]):  #need to check dif words with very similar letters
                return False
            elif compare[0] != compare[1]:
                return False
        return True

def show_possible_matches(my_word):
    output_list = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            output_list.append(word)
    if len(output_list) == 0:
        return "No matches found"
    else:
        return output_list

if __name__ == "__main__":
#    w1 = input("w1 with ___s: ")
#    w2 = input("actual w2: ")
#    w1 = "a_ pl_ "
    w1="abbbbbbb_ "
    print(show_possible_matches(w1))
#    print(match_with_gaps(w1,w2))

