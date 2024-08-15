import sys

def stabilize():
    max_steps = 350

    def take_action(action):
        print(action)
        sys.stdout.flush()

    def get_vitals(vital_signs_times, vital_signs_values):
        return {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

    def check_cardiac_arrest(vitals):
        return (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65
        )
    
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            continue
        
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        vitals = get_vitals(vital_signs_times, vital_signs_values)

        if check_cardiac_arrest(vitals):
            take_action(17)  # Start chest compressions
            continue
        
        if vital_signs_times[5] == 0:
            take_action(25)  # UseSatsProbe
            continue
        if vital_signs_times[4] == 0:
            take_action(27)  # UseBloodPressureCuff
            continue

        if any(events[i] == 0 for i in range(3, 7)):
            take_action(3)  # Examine Airway
            continue
        if any(events[i] == 0 for i in range(7, 15)):
            take_action(4)  # Examine Breathing
            continue
        if any(events[i] == 0 for i in range(15, 37)) or vital_signs_times[0] == 0 or vital_signs_times[1] == 0 or vital_signs_times[4] == 0:
            take_action(5)  # Examine Circulation
            continue
        if any(events[i] == 0 for i in range(21, 25)):
            take_action(6)  # Examine Disability
            continue
        if any(events[i] == 0 for i in range(25, 33)):
            take_action(7)  # Examine Exposure
            continue

        if any(events[i] > 0 for i in range(3, 7)):
            if events[4] > 0 or events[5] > 0:
                take_action(31)  # UseYankeurSuctionCatheter
            elif events[6] > 0:
                take_action(32)  # UseGuedelAirway
            continue
        
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue
        
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue
        
        if vitals["HR"] is not None and (vitals["HR"] < 60 or vitals["HR"] > 100):
            take_action(24)  # UseMonitorPads
            take_action(43)  # DefibrillatorPace
            continue

        take_action(48)  # Finish
        break

if __name__ == "__main__":
    stabilize()