def abbreviate(words):
    words = words.replace("-", " ")
    words_arr = words.split(" ")
    
    accronym = ""
    for word in words_arr:
        accronym += word[0]
           
    return accronym.upper()