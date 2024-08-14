import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    examine_order = [3, 4, 5, 6, 7]

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]

        vitals = {name: value if time > 0 else None 
                  for value, time, name in zip(vital_signs_values, vital_signs_times, 
                  ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"])}

        def take_action(action):
            actions_taken.add(action)
            print(action)

        if 25 not in actions_taken:
            take_action(25)  # UseSatsProbe
            continue
        if 27 not in actions_taken:
            take_action(27)  # UseBloodPressureCuff
            continue
        if 16 not in actions_taken:
            take_action(16)  # ViewMonitor
            continue

        for exam in examine_order:
            if exam not in actions_taken:
                take_action(exam)
                continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)  # StartChestCompression
            continue
        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(22)  # BagDuringCPR
            continue
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        unstable_tachyarrhythmia = any(events[i] > 0 for i in [29, 30, 31, 32])
        if unstable_tachyarrhythmia:
            if 28 not in actions_taken:
                take_action(28)  # AttachDefibPads
                continue
            take_action(40)  # DefibrillatorCharge
            continue

        if all(vital is not None and vital >= threshold for vital, threshold in 
               zip([vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60])):
            take_action(48)  # Finish
            return

        take_action(48)  # Finish
        return

if __name__ == "__main__":
    stabilize()