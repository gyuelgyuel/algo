def solution(babbling):
    answer = 0
    babble_list = ['aya','ye','woo','ma']

    for word in babbling:
        new_babble_list = babble_list.copy()
        if babble_find(new_babble_list, word):
            answer += 1       
    return answer

def babble_find(*listnword):    # input format : <list>, <string>
    finded_word = ''
    finded_bool = False
    if listnword[1] == '':              # when all letter of word deleted by remove babble
        return True
    elif len(listnword[0]) == 0: # when some letter of word remain but babble used least once
        return False
    else:
        babble_list = listnword[0]  # <list>
        word = listnword[1]         # <string>
        for babble in babble_list:  # check if first word is in babble list
            if word.find(babble) == 0:
                finded_word = babble
                finded_bool = True
        if finded_bool:             # if first word is babble word, remove it and find other babble word
            babble_list.remove(finded_word)
            new_babble_list = babble_list.copy()
            new_word = word.replace(finded_word,'')
            return babble_find(new_babble_list,new_word)
        else:                       # when babble word doesn't match
            return False