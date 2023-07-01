#word seperation By Badr

def cap_space(txt):
    # write your code here ^_^
    res='' #intialization 
    for i in txt:
        if i.isupper():
            res+=res.join(' ')
        res+=i
    return res.lower()

print(cap_space('thankYou'))
