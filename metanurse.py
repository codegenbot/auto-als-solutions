import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined_vitals = set()
    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]
        
        if times[0] == 0: 
            take_action(24)
            continue
        if times[1] == 0: 
            take_action(4)
            continue
        if times[4] == 0: 
            take_action(27)
            continue
        if times[5] == 0: 
            take_action(25)
            continue
        
        vitals = {
            "HR": values[0],
            "RR": values[1],
            "Glucose": values[2],
            "Temp": values[3],
            "MAP": values[4],
            "Sats": values[5],
            "Resps": values[6],
        }

        if vitals["Sats"] < 65 or vitals["MAP"] < 20:
            take_action(17)
            continue

        if events[3] == 0 and events[8] == 0:
            take_action(3)
            continue
        
        if vitals["Sats"] < 88: 
            take_action(30)
            continue
        
        if vitals["RR"] < 8:
            take_action(29)
            continue
        
        if vitals["MAP"] < 60:
            take_action(15)
            continue
        
        if vitals["HR"] < 60 or vitals["HR"] > 150:
            take_action(9)
            continue

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()