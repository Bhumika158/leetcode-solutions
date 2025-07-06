size=3
import string

def print_rangoli(size):
    # alpha= string.ascii_lowercase
    # lines=[]
    # width = 4*size -3
    # for i in range(size):
    #     s= "-".join(alpha[size-1:i:-1]+ alpha[i:size])
    #     lines.append(s.center(width,"-"))
    #
    # a = lines[::-1]
    # b= a[:2][::-1]
    # pattern = a+b
    #
    # for line in pattern:
    #     print(line)

    width = 4*size -3
    line=[]
    for i in range(size):
        left_seq = [chr(97+size-1-j) for j in range(i+1)]
        right_seq= left_seq[:-1][::-1]
        full_seq = "-".join(left_seq+right_seq)
        line.append(full_seq.center(width,"-"))
    pattern = line + line[-2::-1]

    for l in pattern:
        print(l)

print_rangoli(size)
