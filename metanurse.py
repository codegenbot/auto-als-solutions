import sys

used_methods = {
    "UsedSatsProbe": False,
    "ViewedMonitor": False,
    "OpenedBreathingDrawer": False,
    "OpenedCirculationDrawer": False,
    "UsedMonitorPads": False,
    "UsedBP_Cuff": False,
    "UsedA_Line": False,
    "GivenFluids": False,
    "UsedDefibPads": False,
    "DefibrillatorCharged": False,
}

def next_action(observations):
    events = observations[:33]
    vital_signs_times = observations[33:40]
    vital_signs_values = observations[40:]

    vitals = {
        name: value if time > 0 else None
        for time, value, name in zip(vital_signs_times, vital_signs_values, [
            "HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"
        ])
    }

    if not events[3]:  # AirwayClear
        return 3  # ExamineAirway

    if not used_methods["OpenedBreathingDrawer"]:
        used_methods["OpenedBreathingDrawer"] = True
        return 19  # OpenBreathingDrawer

    if not used_methods["UsedSatsProbe"]:
        used_methods["UsedSatsProbe"] = True
        return 25  # UseSatsProbe

    if not used_methods["ViewedMonitor"]:
        used_methods["ViewedMonitor"] = True
        return 16  # ViewMonitor

    if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
        return 17  # StartChestCompression

    if vitals["Sats"] and vitals["Sats"] < 88:
        return 30  # UseNonRebreatherMask

    if vitals["RespRate"] and vitals["RespRate"] < 8:
        return 29  # UseBagValveMask

    if vitals["MAP"] and vitals["MAP"] < 60:
        if not used_methods["OpenedCirculationDrawer"]:
            used_methods["OpenedCirculationDrawer"] = True
            return 20  # OpenCirculationDrawer
        if not used_methods["UsedBP_Cuff"]:
            used_methods["UsedBP_Cuff"] = True
            return 27  # UseBloodPressureCuff
        if not used_methods["GivenFluids"]:
            used_methods["GivenFluids"] = True
            return 15  # GiveFluids

    if vitals["HeartRate"]:
        if vitals["HeartRate"] < 50:
            return 12  # GiveAtropine
        elif 100 < vitals["HeartRate"] <= 150:
            return 2  # CheckRhythm
        elif vitals["HeartRate"] > 150:
            if not used_methods["UsedDefibPads"]:
                used_methods["UsedDefibPads"] = True
                return 28  # AttachDefibPads
            if not used_methods["DefibrillatorCharged"]:
                used_methods["DefibrillatorCharged"] = True
                return 40  # DefibrillatorCharge
            return 44  # DefibrillatorPacePause

    return 48  # Finish

def main():
    max_steps = 350
    for _ in range(max_steps):
        observations = list(map(float, input().strip().split()))
        action = next_action(observations)
        print(action)
        if action == 48:
            break

if __name__ == "__main__":
    main()