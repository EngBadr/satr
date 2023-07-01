#number to its relative string

def numToEng(n: int) -> str:
    # write your code here ^_^
    ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = [
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]
    ordinal = [
        "ten",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]
    hundreds = "hundred"
    hund = ""
    rest = ""
    res = ""
    last_num = ""
    tens_numbr = ""
    val = str(n)
    if n < 999:
        if len(val) == 3:
            if int(val[0]) in range(0, len(ones) + 1):
                hund = ones[int(val[0]) - 1]
                rest += (val[1]) + (val[2])
                if rest == "00":
                    res = hund + " " + hundreds
                else:
                    res = hund + " " + hundreds + " " + numToEng(int(rest))
        elif len(val) == 2:
            if int(val[1]) == 0:
                tens_numbr = ordinal[int(val[0]) - 1]
                res = tens_numbr
            else:
                if int(val[0]) in range(0, len(ordinal) + 1) and int(val[0]) != 1:
                    tens_numbr = ordinal[int(val[0]) - 1]
                    rest += val[1]
                    res = tens_numbr + "-" + numToEng(int(rest))
                elif int(val[0]) == 1 and (int(val[1]) in range(0, len(tens) + 1)):
                    tens_numbr = tens[int(val[1]) - 1]
                    res = tens_numbr
        elif len(val) == 1:
            if int(val[0]) == 0:
                res = "zero"
            elif int(val[0]) in range(0, len(ones) + 1) and int(val[0]) != 0:
                last_num = ones[int(val[0]) - 1]
                res = last_num
    return str(res)
print(numToEng(460))
