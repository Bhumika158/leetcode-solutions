def count_substring(string, sub_string):
    l,r,c= 0,len(sub_string),0
    print(l,r,c)
    while r <= len(string):
        if string[l:r] == sub_string:
            c+=1
        l+=1
        r+=1
    return c


if __name__ == '__main__':
    string = input("provide the input").strip()
    sub_string = input("provide the substring").strip()

    count = count_substring(string, sub_string)
    print(count)