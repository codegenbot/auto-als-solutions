import sys

def main():
    ACTIONS = [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 
        19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 
        35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48
    ]

    max_steps = 350
    step = 0
    used_methods = set()

    while step < max_steps:
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:]
        )

        vitals = {name: value if time > 0 else None for value, time, name in zip(
            vital_signs_values,
            vital_signs_times,
            ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"]
        )}

        if step == 0:
            print(ACTIONS[3])  # ExamineAirway
        elif not events[3]:  # AirwayClear event
            print(ACTIONS[35])  # PerformAirwayManoeuvres
        elif "UseSatsProbe" not in used_methods:
            print(ACTIONS[25])  # UseSatsProbe
            used_methods.add("UseSatsProbe")
        elif "UseBloodPressureCuff" not in used_methods:
            print(ACTIONS[27])  # UseBloodPressureCuff
            used_methods.add("UseBloodPressureCuff")
        elif not vitals["MAP"]:
            print(ACTIONS[38])  # TakeBloodPressure
        elif not vitals["Sats"]:
            print(ACTIONS[16])  # ViewMonitor
        elif (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            print(ACTIONS[17])  # StartChestCompression
        elif vitals["MAP"] and vitals["MAP"] < 60:
            print(ACTIONS[15])  # GiveFluids
        elif vitals["Sats"] and vitals["Sats"] < 88:
            print(ACTIONS[30])  # UseNonRebreatherMask
        elif vitals["RespRate"] and vitals["RespRate"] < 8:
            print(ACTIONS[29])  # UseBagValveMask
        elif vitals["HeartRate"] and (vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50):
            if "TurnOnDefibrillator" not in used_methods:
                print(ACTIONS[39])  # TurnOnDefibrillator
                used_methods.add("TurnOnDefibrillator")
            elif "DefibrillatorCurrentUp" not in used_methods:
                print(ACTIONS[41])  # DefibrillatorCurrentUp
                used_methods.add("DefibrillatorCurrentUp")
            else:
                print(ACTIONS[43])  # DefibrillatorPace
        elif all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
            )
        ):
            print(ACTIONS[48])  # Finish
            return
        else:
            print(ACTIONS[0])  # DoNothing

        step += 1  # Increment step counter

if __name__ == "__main__":
    main()