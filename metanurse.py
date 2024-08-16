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

        vitals = {
            "HR": values[0] if times[0] != 0 else None,
            "RR": values[1] if times[1] != 0 else None,
            "Glucose": values[2] if times[2] != 0 else None,
            "Temp": values[3] if times[3] != 0 else None,
            "MAP": values[4] if times[4] != 0 else None,
            "Sats": values[5] if times[5] != 0 else None,
            "Resps": values[6] if times[6] != 0 else None,
        }

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)  # StartChestCompression
            continue

        if any(events[i] > 0 for i in range(3, 7)) and "airway" not in examined_vitals:
            take_action(3)  # ExamineAirway
            examined_vitals.add("airway")
            continue
        
        if vitals["Sats"] is None and "Sats" not in examined_vitals:
            take_action(25)  # UseSatsProbe
            examined_vitals.add("Sats")
            continue
        
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue
        
        if vitals["RR"] is None and "RR" not in examined_vitals:
            take_action(4)  # ExamineBreathing
            examined_vitals.add("RR")
            continue
        
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue
        
        if vitals["MAP"] is None and "MAP" not in examined_vitals:
            take_action(27)  # UseBloodPressureCuff
            examined_vitals.add("MAP")
            continue
        
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue
        
        if events[15] > 0 and "circulation" not in examined_vitals:
            take_action(5)  # ExamineCirculation
            examined_vitals.add("circulation")
            continue
        
        if vitals["HR"] is not None and (vitals["HR"] < 60 or vitals["HR"] > 100):
            take_action(2)  # CheckRhythm
            continue
        
        if events[28] > 0 or events[30] > 0:
            take_action(9)  # GiveAdenosine
            continue
        
        if any(events[i] > 0 for i in range(20, 26)) and "disability" not in examined_vitals:
            take_action(6)  # ExamineDisability
            examined_vitals.add("disability")
            continue
        
        if any(events[i] > 0 for i in range(26, 33)):
            take_action(7)  # ExamineExposure
            continue
        
        take_action(48)  # Finish
        break

if __name__ == "__main__":
    stabilize()