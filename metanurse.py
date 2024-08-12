import sys

def main():
    max_steps = 350
    used_actions = {19: False, 20: False, 25: False, 26: False, 27: False}
    steps = 0

    def perform_action(action):
        nonlocal steps
        print(action)
        steps += 1

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        # Extract vitals if measured
        vital_sign_names = ["HeartRate", "RespRate", "CapillaryGlucose", 
                            "Temperature", "MAP", "Sats", "Resps"]
        vitals = {
            name: value if time > 0 else None
            for value, time, name in zip(vital_signs_values, vital_signs_times, vital_sign_names)
        }

        if not events[3]:  # No AirwayClear
            perform_action(3)  # ExamineAirway
            continue
        
        if vitals["Sats"] is not None and vitals["Sats"] < 65 or vitals["MAP"] is not None and vitals["MAP"] < 20:
            perform_action(17)  # StartChestCompression
            continue

        if not used_actions[19]:  # BreathingDrawer Not opened
            perform_action(19)  # OpenBreathingDrawer
            used_actions[19] = True
            continue

        if not used_actions[25]:
            perform_action(25)  # UseSatsProbe
            used_actions[25] = True
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            perform_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            perform_action(29)  # UseBagValveMask
            continue

        if not used_actions[20]:  # CirculationDrawer Not opened
            perform_action(20)  # OpenCirculationDrawer
            used_actions[20] = True
            continue

        if not used_actions[27]:  # UseBloodPressureCuff not used
            perform_action(27)  # UseBloodPressureCuff
            used_actions[27] = True
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            perform_action(15)  # GiveFluids
            continue

        perform_action(48)  # Finish
        break

    if steps >= max_steps:
        perform_action(48)  # Finish if max steps reached

if __name__ == "__main__":
    main()