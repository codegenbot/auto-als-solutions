import sys

def prioritize_actions(events, vitals):
    if vitals["Sats"] is None:
        return 25  # UseSatsProbe
    if vitals["MAP"] is None:
        return 27  # UseBloodPressureCuff
    if None in (vitals["RespRate"], vitals["MAP"], vitals["Sats"]):
        return 16  # ViewMonitor
    if not events[3:7].count(0):  # Airway related events AirwayClear, AirwayVomit, AirwayBlood, AirwayTongue
        return 3  # ExamineAirway
    if not events[7:15].count(0):  # Breathing related events
        return 4  # ExamineBreathing

    if vitals["MAP"] < 20 or vitals["Sats"] < 65:
        return 17  # StartChestCompression
    if vitals["MAP"] < 60:
        return 15  # GiveFluids
    if vitals["Sats"] < 88:
        return 30  # UseNonRebreatherMask
    if vitals["RespRate"] < 8:
        return 29  # UseBagValveMask

    return 48  # Finish

def stabilize():
    max_steps = 350

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:]
        )
        
        vitals = {
            name: value if time > 0 else None
            for value, time, name in zip(
                vital_signs_values,
                vital_signs_times,
                [
                    "HeartRate",
                    "RespRate",
                    "CapillaryGlucose",
                    "Temperature",
                    "MAP",
                    "Sats",
                    "Resps"
                ]
            )
        }

        action = prioritize_actions(events, vitals)
        print(action)
        if action == 48:
            break

if __name__ == "__main__":
    stabilize()