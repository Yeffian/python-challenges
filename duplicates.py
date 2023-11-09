def remove_duplicates(n):
    result = [] 

    for i in n:
        if i in result:
            pass
        else:
            result.append(i)
    
    return result
