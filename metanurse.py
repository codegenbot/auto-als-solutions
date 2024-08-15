import sys

def stabilize():
    max_steps = 350
    
    def take_action(action):
        print(action)
        actions_taken.add(action)
    
    actions_taken = set()
    required_measurements = [24, 25, 27]  # UseMonitorPads, UseSatsProbe, UseBloodPressureCuff
    
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:]
        )
    
        vitals = {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }
    
        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(17)  # StartChestCompression
            continue
    
        for action in required_measurements:
            if action not in actions_taken:
                take_action(action)
                break
        
        if any(events[i] > 0 for i in range(3, 7)):  # Airway-related events
            take_action(3)  # ExamineAirway
            if events[4] > 0 or events[5] > 0:  # Vomit or Blood in Airway
                take_action(31)  # UseYankeurSucionCatheter
            elif events[6] > 0:  # Tongue in Airway
                take_action(32)  # UseGuedelAirway
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue
    
        if any(events[i] > 0 for i in range(7, 15)):  # Breathing-related events
            take_action(4)  # ExamineBreathing
            if events[7] > 0:  # BreathingNone
                take_action(29)  # UseBagValveMask
            continue
    
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue
    
        if any(events[i] > 0 for i in [20, 21, 22]):  # AVPU-related events
            take_action(6)  # ExamineDisability
            continue
    
        if any(events[i] > 0 for i in [25, 26, 27]):  # Exposure-related events
            take_action(7)  # ExamineExposure
            continue
    
        if action in actions_taken:
            take_action(48)  # Finish
            break

if __name__ == "__main__":
    stabilize()