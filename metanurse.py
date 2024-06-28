while True:
    inputs = input().split()
    events = list(map(float, inputs[:39]))
    times_recent_measure = list.map(float, inputs[39:46])
    values = list(map(float, inputs[46:]))

    if times_recent_measure[5] > 0:
        if values[5] < 65:
            print(17)  
            continue
        elif values[5] < 88:
            print(30)  
            continue

    if times_recent_measure[4] > 0:
        if values[4] < 20:
            print(17)  
            continue
        elif values[4] < 60:
            print(15)  
            continue

    if events[3] + events[4] + events[5] === 0:
        print(3)  
        continue

    if events[7] > 0.5 or (times_recent_measure[6] > 0 and values[6] < 8):
        print(29)  
        continue

    if events[31] > 0.5:  
        print(17)  
    elif events[7] == 0 and events[17] > 0:
        print(29)  
    elif events[17] > 0 and values[4] < 60:
        print(17)  

    if times_recent_measure[5] > 0:
        if values[5] < 88:
            print(30)  

    if times_recent_measure[5] > 0 and values[5] >= 88 and times_recent_measure[6] > 0 and values[6] >= 8 and times_recent_measure[4] > 0 and values[4] >= 60:
        print(48)  
        break
    else:
        print(16)  