# given string, reverse string with arbitary spaces between each word while maintaining order of each word

def reverseOrder(data):
    wordList = data.split()
    ans = ""
    
    i = 0
    j = len(data)-1
    while j >= 0:
        if data[j] == " ": 
            ans += " "
            j -= 1
        else:
            word = wordList.pop()
            ans += word
            while j >= 0 and data[j] != " ": j -= 1
    return ans


print(reverseOrder("abc"))
print(reverseOrder("abc def"))
print(reverseOrder("abc.  def a.    ert"))
            
