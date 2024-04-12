# convert a string into numeric value

m = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, 
        "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}

def convert(s):
    ans = 0
    neg, decimal = False, 0
    decCount = 0
    
    for i, c in enumerate(s):
        if decimal == 1 and c.isdigit():
            decCount += 1
            ans += float(m[s[i]]) / pow(10, decCount)
        elif c.isdigit():
            ans *= 10
            ans += m[s[i]]
        elif c == "-" and i == 0 and i+1 < len(s) and s[i+1] in m: 
            neg = True
        elif c == "." and decimal == 0 and \
        ((i-1 >= 0 and s[i-1] in m) or (i+1 < len(s) and s[i+1] in m)): 
            decimal += 1
        else:
            return "error"
    
    return (-1 * ans) if neg else ans

print(convert("123450.1123"))
        
