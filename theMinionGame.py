def minion_game(string):
    vow= 'AEIOU'
    k_score,s_score =0,0
    length=len(string)
    for i in range(length):
        if string[i] in vow:
            k_score += length-i
        else:
            s_score += length -i
    if k_score > s_score:
        print("Kevin",k_score)
    elif s_score > k_score:
        print("Stuart",s_score)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)