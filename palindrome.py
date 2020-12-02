def main():
    s = str(input('Please provide a word : '))
    str_len = len(s)
    pal = True
    if str_len == 1:
        print('Length = 1')
    else:
        alist = []
        for i in range(str_len - 1, -1, -1):  # str_len - 1 because otherwise its out of bounds.
            alist.append(s[i])
        for i in range(str_len):
            if s[i] != alist[i]:
                pal = False
        if pal:
            adict = {s: str_len}
            print(adict)
            print(alist)
        else:
            print('Not a palindrome')


if __name__ == '__main__':
    main()
