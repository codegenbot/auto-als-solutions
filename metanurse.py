import sys

def stabilize():
    max_steps = 350
    def get_action_by_protocol(observations):
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )
        vitals = {name: value if time > 0 else None
                  for value, time, name in zip(vital_signs_values, vital_signs_times,
                                               ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature",
                                                "MAP", "Sats", "Resps"])}

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            return 17  # StartChestCompression

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            return 17  # StartChestCompression

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            return 15  # GiveFluids

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            return 30  # UseNonRebreatherMask

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            return 29  # UseBagValveMask
        
        if vitals["HeartRate"] is not None and (vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50):
            return 24  # UseMonitorPads

        if all(vital is not None and vital >= threshold for vital, threshold in zip(
            [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60])):
            return 48  # Finish

        return 16  # ViewMonitor (continue monitoring)

    first_examine = False
    use_sats_probe = use_blood_pressure_cuff = False

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        
        if not first_examine:
            first_examine = True
            print(3)  # ExamineAirway
            continue

        if not use_sats_probe:
            print(25)  # UseSatsProbe
            use_sats_probe = True
            continue
        
        if not use_blood_pressure_cuff:
            print(27)  # UseBloodPressureCuff
            use_blood_pressure_cuff = True
            continue

        action = get_action_by_protocol(observations)
        print(action)
        if action == 48:
            return

if __name__ == "__main__":
    stabilize()