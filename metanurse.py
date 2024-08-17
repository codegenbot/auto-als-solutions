import sys

DO_NOTHING, EXAMINE_AIRWAY, EXAMINE_BREATHING, EXAMINE_CIRCULATION, USE_BP_CUFF, USE_SATS_PROBE, USE_NON_REBREATHER_MASK, GIVE_FLUIDS, PERFORM_CARDIOVERSION, FINISH = 0, 3, 4, 5, 27, 25, 30, 15, 24, 48

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    steps, examined, monitor_checked = 350, set(), False
    for step in range(steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(DO_NOTHING)
            continue

        events, measuring_times, measurements = observations[:33], observations[33:40], observations[46:]
        vitals = ["HR", "RR", "Glucose", "Temp", "MAP", "Sats", "Resps"]
        vitals_dict = {vitals[i]: measurements[i] if measuring_times[i] > 0 else None for i in range(7)}

        if (vitals_dict["Sats"] and vitals_dict["Sats"] < 65) or (vitals_dict["MAP"] and vitals_dict["MAP"] < 20):
            take_action(PERFORM_CARDIOVERSION)
            continue

        if not any(events[3:7]) and "Airway" not in examined:
            take_action(EXAMINE_AIRWAY)
            examined.add("Airway")
            continue

        if "Sats" not in examined and vitals_dict["Sats"] is None:
            take_action(USE_SATS_PROBE)
            examined.add("Sats")
            continue

        if "MAP" not in examined and vitals_dict["MAP"] is None:
            take_action(USE_BP_CUFF)
            examined.add("MAP")
            continue

        if "Breathing" not in examined:
            take_action(EXAMINE_BREATHING)
            examined.add("Breathing")
            continue

        if not monitor_checked:
            take_action(EXAMINE_CIRCULATION)
            monitor_checked = True
            continue

        if vitals_dict["Sats"] and vitals_dict["Sats"] < 88:
            take_action(USE_NON_REBREATHER_MASK)
            continue

        if vitals_dict["MAP"] and vitals_dict["MAP"] < 60:
            take_action(GIVE_FLUIDS)
            continue

        if vitals_dict["RR"] and vitals_dict["RR"] < 8:
            take_action(USE_NON_REBREATHER_MASK)
            continue

        if vitals_dict["HR"]:
            if vitals_dict["HR"] > 150:
                take_action(PERFORM_CARDIOVERSION)
                continue
            elif vitals_dict["HR"] < 50:
                take_action(GIVE_FLUIDS)
                continue

        take_action(FINISH)
        break
    else:
        take_action(FINISH)

if __name__ == "__main__":
    stabilize()