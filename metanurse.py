import sys

def stabilize():
    max_steps = 350
    steps = 0

    def perform_step(action):
        nonlocal steps
        print(action)
        steps += 1
        if steps >= max_steps:
            print(48)  # Finish
            sys.exit()

    while steps < max_steps:
        observations = list(map(float, input().strip().split()))
        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]
        
        vitals = {name: value if time > 0 else None for value, time, name in zip(
            vital_signs_values, vital_signs_times, ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"])}

        # Simulate initial ABCDE check routines
        if steps == 0:
            perform_step(3)  # ExamineAirway
            continue
        if steps == 1:
            perform_step(25)  # UseSatsProbe
            continue
        if steps == 2:
            perform_step(16)  # ViewMonitor
            continue
        if steps == 3:
            perform_step(27)  # UseBloodPressureCuff
            continue
            
        # Vital actions based on assessments
        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            perform_step(17)  # StartChestCompression
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            perform_step(17)  # StartChestCompression
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            perform_step(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            perform_step(29)  # UseBagValveMask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            perform_step(15)  # GiveFluids
            continue

        if vitals["HeartRate"] is not None and (vitals["HeartRate"] > 150 or events[32] > 0):
            perform_step(40)  # DefibrillatorCharge
            continue

        if all(vital is not None and vital >= threshold for vital, threshold in zip([vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60])):
            perform_step(48)  # Finish
            return

        perform_step(0)  # DoNothing
        
if __name__ == "__main__":
    stabilize()