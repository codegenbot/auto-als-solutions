import sys

def main():
    max_steps = 350
    used_methods = set()

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
                vital_signs_values, vital_signs_times,
                ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"]
            )
        }

        # A - Airway
        if "ExamineAirway" not in used_methods:
            print(3)
            used_methods.add("ExamineAirway")
            continue
        if not events[3]:  # Airway is not clear
            if events[4]:  # AirwayVomit
                print(31)  # UseYankeurSuctionCatheter
            elif events[5]:  # AirwayBlood
                print(31)  # UseYankeurSuctionCatheter
            elif events[6]:  # AirwayTongue
                print(36)  # PerformHeadTiltChinLift
            else:
                print(35)  # PerformAirwayManoeuvres
            continue

        # B - Breathing
        if "ExamineBreathing" not in used_methods:
            print(4)
            used_methods.add("ExamineBreathing")
            continue
        if "OpenBreathingDrawer" not in used_methods:
            print(19)
            used_methods.add("OpenBreathingDrawer")
            continue
        if "UseSatsProbe" not in used_methods:
            print(25)
            used_methods.add("UseSatsProbe")
            continue
        if "ViewMonitor" not in used_methods:
            print(16)
            used_methods.add("ViewMonitor")
            continue
        if vitals["Sats"]:
            if vitals["Sats"] < 65:
                print(17)  # StartChestCompression
                continue
            elif vitals["Sats"] < 88:
                print(30)  # UseNonRebreatherMask
                continue
        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        # C - Circulation
        if "ExamineCirculation" not in used_methods:
            print(5)
            used_methods.add("ExamineCirculation")
            continue
        if "UseBloodPressureCuff" not in used_methods:
            print(27)
            used_methods.add("UseBloodPressureCuff")
            continue
        if "ViewMonitorCirculation" not in used_methods:
            print(16)
            used_methods.add("ViewMonitorCirculation")
            continue
        if vitals["MAP"]:
            if vitals["MAP"] < 20:
                print(17)  # StartChestCompression
                continue
            elif vitals["MAP"] < 60:
                print(15)  # GiveFluids
                continue
        if vitals["HeartRate"]:
            if vitals["HeartRate"] < 50:
                print(12)  # GiveAtropine
                continue
            elif vitals["HeartRate"] > 100:
                print(2)  # CheckRhythm
                continue

        # If all vitals are stable, finish the scenario
        if vitals["Sats"] >= 88 and vitals["RespRate"] >= 8 and vitals["MAP"] >= 60:
            print(48)  # Finish
            return

    print(48)  # Finish after max_steps

if __name__ == "__main__":
    main()