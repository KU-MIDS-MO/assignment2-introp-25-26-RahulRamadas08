def breakdown_time(seconds):
    if (type(seconds) != int) or (seconds < 0):
        return -1
    else:
        if seconds == 0:
            return {}
        else:
            dictio = {}
            if seconds % 3600 == 0:
                dictio[3600] = seconds/3600
            else:
                if seconds % 60 == 0:
                    dictio[3600] = seconds//3600
                    dictio[60] = (seconds % 3600) / 60
                else:
                    dictio[3600] = seconds//3600
                    dictio[60] = (seconds % 3600) // 60
                    dictio[1] = seconds % 60
            return dictio
    
    
