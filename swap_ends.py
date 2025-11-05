def swap_ends(L, k):
    newlist = L
    if (k <= 0) or (len(L) ==0) or (k > (len(L) / 2)):
        return (newlist, 0)
    else:
        num_swaps = 0
        
        front = []
        middle = []
        end = []
        
        for i in range(k):
            front.append(L[i])
        for i in range(k, len(L) - k):
            middle.append(L[i])
        for i in range(len(L) - k, len(L)):
            end.append(L[i])
        
        newlist = end + middle + front
        
        return (newlist, k)

