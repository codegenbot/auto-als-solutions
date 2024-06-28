while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if not any(measured_times):  
        print(8)  
    else:
        if (measured_times[5] > 0 and measured_values[5] < 65) or (measured_times[4] > 0 and measured_values[4] < 20):
            print(17)  
        elif events[3] < 0.5:
            print(3)  
        elif measured_values[5] < 88:
            print(30)  
        elif measured_values[4] < 60:
            print(15)  
        elif events[22] > 0.5:
            print(6)  
        elif measured_values[5] >= 88 and measured_values[6] >= 8 and measured_values[4] >= 60:
            print(48)  
            break
        else:
            print(16)  