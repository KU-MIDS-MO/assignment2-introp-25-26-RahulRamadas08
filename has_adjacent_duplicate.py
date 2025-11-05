def has_adjacent_duplicate(L):
    if len(L) <= 1:
        return False
    else:
        val = False
        
        for i in range(len(L) - 1):
            if L[i] == L[i+1]:
                val = True
        return val
            
