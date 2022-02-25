def decode_morse(morse_code, MORSE_CODE):
    singleWord = ""
    phrase = ""
    subStrStart = 0
    i = 0

    morse_code = removeSurroundingSpaces(morse_code)

    while i < len(morse_code):
        if morse_code[i] == " ":
            singleWord += MORSE_CODE[morse_code[subStrStart:i]]
            subStrStart = i + 1
            if morse_code[i+1] == " ":
                phrase += singleWord + " "
                singleWord = ""
                subStrStart = i + 3
                i = i + 2 # 2 not three, since 1 more is added at the end of the loop

        elif (i + 1) == len(morse_code):
            singleWord += MORSE_CODE[morse_code[subStrStart:i+1]]
            phrase += singleWord 

        i += 1
 
    return phrase

def removeSurroundingSpaces(morse_code):
    if morse_code[0] == " ":
        i = 0
        leftSideSpacesExist = True
        while leftSideSpacesExist:
            if morse_code[i] == " ":
                i += 1
            else:
                leftSideSpacesExist = False
        
        morse_code = morse_code[i:len(morse_code)]
    
    if morse_code[len(morse_code)-1] == " ":
        i = len(morse_code) - 1
        rightSideSpacesExist = True
        while rightSideSpacesExist:
            if morse_code[i] == " ":
                i -= 1
            else:
                rightSideSpacesExist = False
        
        morse_code = morse_code[0:i+1]

    return morse_code

def xo(s):
    numX = 0
    numO = 0
    
    for char in s:
        if char == "x" or char =="X":
            numX += 1
        elif char == "o" or char == "O":
            numO += 1
    
    # print("numX:", numX)
    # print("numO:", numO)

    if numX == 0 and numO == 0:
        return False
    elif numX == numO:
        return True
    
    return False

def array_diff(a, b):
    for val in b:
        if val in a:
            a = [s for s in a if s != val]
            print(a)
    
    return a


if __name__ == "__main__":
    # print(array_diff([1,2,3], [1, 2]))
    # print(type(1))

    # if type(1) == int:
    #     print(True)
    # print(xo('xo'))
    # print(xo("xo0"))

    MORSE_CODE = {
        ".-": "A",
        "-...": "B",
        "-.-.": "C",
        "-..": "D",
        ".": "E",
        "..-.": "F",
        "--.": "G",
        "....": "H",
        "..": "I",
        ".---": "J",
        "-.-": "K",
        ".-..": "L",
        "--": "M",
        "-.": "N",
        "---": "O",
        ".--.": "P",
        "--.--": "Q",
        ".-.": "R",
        "...": "S",
        "-": "T",
        "..-": "U",
        "...-": "V",
        ".--": "W",
        "-..-": "X",
        "-.--": "Y",
        "--..": "Z"
    }  

    m_code1 = ".... . -.--   .--- ..- -.. ." # HEY JUDE
    m_code2 = ".... . -.--   .--- ..- -.. .   .... .." # HEY JUDE HI
    m_code3 = "... --- ..." # SOS
    m_code4 = " . " # E
    print(decode_morse(m_code4, MORSE_CODE))