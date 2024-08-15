import sys

def stabilize():
    max_steps = 350
    step = 0
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)

    required_measurements = [24, 25, 27]  # UseMonitorPads, UseSatsProbe, UseBloodPressureCuff

    def next_measurement_action():
        for action in required_measurements:
            if action not in actions_taken:
                return action

    def needs_measurements():
        return not all(action in actions_taken for action in required_measurements)

    while step < max_steps:
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            continue

        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        vitals = {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        # Immediate cardiac arrest intervention
        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65
        ):
            take_action(17)  # Start chest compressions
            step += 1
            continue

        # Ensure measurements are taken
        if needs_measurements():
            take_action(next_measurement_action())
            step += 1
            continue

        # Airway
        if any(events[i] > 0 for i in range(3, 7)):
            take_action(3)  # Examine airway
            if events[4] > 0 or events[5] > 0:
                take_action(31)  # Use suction catheter
            elif events[6] > 0:
                take_action(32)  # Use Guedel airway
            step += 1
            continue

        # Breathing
        if (vitals["Sats"] is not None and vitals["Sats"] < 88) or (vitals["RR"] is not None and vitals["RR"] < 8):
            if vitals["Sats"] is not None and vitals["Sats"] < 88:
                take_action(30)  # Use non-rebreather mask
            if vitals["RR"] is not None and vitals["RR"] < 8:
                take_action(29)  # Use bag valve mask
            step += 1
            continue

        if any(events[i] > 0 for i in range(7, 15)):
            take_action(4)  # Examine breathing
            step += 1
            continue

        # Circulation
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give fluids
            step += 1
            continue

        tachyarrhythmias = ["HeartRhythmSVT", "HeartRhythmVT", "HeartRhythmAF",
                            "HeartRhythmAtrialFlutter", "HeartRhythmTorsades", "HeartRhythmVF"]
        if any(events[i] > 0 for i in [27 + i for i in range(len(tachyarrhythmias))]):
            take_action(24)  # Use monitor pads
            take_action(43)  # Defibrillator pace
            step += 1
            continue

        if any(events[i] > 0 for i in range(15, 20)):
            take_action(5)  # Examine circulation
            step += 1
            continue
        
        # Disability
        if any(events[i] > 0 for i in range(20, 26)):
            take_action(6)  # Examine disability
            step += 1
            continue
            
        # Exposure
        if any(events[i] > 0 for i in range(26, 33)):
            take_action(7)  # Examine exposure
            step += 1
            continue

        # If we have checked all and stabilized, finish
        take_action(48)  # Finish scenario
        break
    
        step += 1

if __name__ == "__main__":
    stabilize()