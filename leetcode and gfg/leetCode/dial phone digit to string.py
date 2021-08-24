def main (digits) :
        dic_t = {'2': [97,98,99],
        '3': [100,101,102],
        '4': [103,104,105],
        '5': [106,107,108],
        '6': [109,110,111],
        '7': [112,113,114,115],
        '8': [116,117,118],
        '9': [119,120,121,122]}

        if len(digits) < 1 : return []
        ans = [""]
        for ch in digits :
            temp  = []
            for old in ans : 
                for x in dic_t[ch]  : 
                    temp.append(old + chr(x))
            ans = temp
        return ans






digits = "23"
print(main(digits))


def test_func1() :
    digits = "23"
    assert main(digits) == ["ad","ae","af","bd","be","bf","cd","ce","cf"]


def test_func2():
    assert main("") == []

