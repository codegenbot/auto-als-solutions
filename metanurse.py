import sys

(
    DO_NOTHING,
    CHECK_LIFE_SIGNS,
    CHECK_RHYTHM,
    EXAMINE_AIRWAY,
    EXAMINE_BREATHING,
    EXAMINE_CIRCULATION,
) = (0, 1, 2, 3, 4, 5)
EXAMINE_DISABILITY, EXAMINE_EXPOSURE, EXAMINE_RESPONSE = 6, 7, 8
GIVE_ADENOSINE, GIVE_ADRENALINE, GIVE_AMIODARONE, GIVE_ATROPINE = 9, 10, 11, 12
GIVE_MIDAZOLAM, USE_VENFLON, GIVE_FLUIDS, VIEW_MONITOR = 13, 14, 15, 16
START_CHEST_COMPRESSION, OPEN_AIRWAY_DRAWER, OPEN_BREATHING_DRAWER = 17, 18, 19
OPEN_CIRCULATION_DRAWER, OPEN_DRUGS_DRAWER, BAG_DURING_CPR = 20, 21, 22
RESUME_CPR, USE_MONITOR_PADS, USE_SATS_PROBE, USE_ALINE = 23, 24, 25, 26
USE_BP_CUFF, ATTACH_DEFIB_PADS, USE_BAG_VALVE_MASK = 27, 28, 29
USE_NON_REBREATHER_MASK, USE_YANKEUR_SUCTION, USE_GUEDEL_AIRWAY = 30, 31, 32
TAKE_BLOOD_GAS, TAKE_BLOODS, PERFORM_AIRWAY_MANEUVER = 33, 34, 35
PERFORM_HEAD_TILT, PERFORM_JAW_THRUST, TAKE_BP = 36, 37, 38
TURN_ON_DEFIB, DEFIB_CHARGE, DEFIB_CURRENT_UP = 39, 40, 41
DEFIB_CURRENT_DOWN, DEFIB_PACE, DEFIB_PACE_PAUSE = 42, 43, 44
DEFIB_RATE_UP, DEFIB_RATE_DOWN, DEFIB_SYNC, FINISH = 45, 46, 47, 48

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    steps, examined = 350, set()
    for step in range(steps):
        try:
            observations = list(map(float, input().strip().split()))
        except:
            take_action(FINISH)
            return
        if len(observations) != 53:
            take_action(DO_NOTHING)
            continue

        events, measuring_times, measurements = (
            observations[:33],
            observations[33:40],
            observations[46:],
        )
        vitals = ["HR", "RR", "Glucose", "Temp", "MAP", "Sats", "Resps"]
        vitals_dict = {
            vitals[i]: measurements[i] if measuring_times[i] > 0 else None
            for i in range(7)
        }

        if (vitals_dict["Sats"] and vitals_dict["Sats"] < 65) or (
            vitals_dict["MAP"] and vitals_dict["MAP"] < 20
        ):
            take_action(START_CHEST_COMPRESSION)
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

        if vitals_dict["Sats"] and vitals_dict["Sats"] < 88:
            take_action(USE_NON_REBREATHER_MASK)
            continue

        if "Circulation" not in examined:
            take_action(EXAMINE_CIRCULATION)
            examined.add("Circulation")
            continue

        if vitals_dict["MAP"] and vitals_dict["MAP"] < 60:
            take_action(GIVE_FLUIDS)
            continue

        if vitals_dict["RR"] and vitals_dict["RR"] < 8:
            take_action(USE_BAG_VALVE_MASK)
            continue

        if vitals_dict["HR"]:
            if vitals_dict["HR"] > 150:
                take_action(USE_MONITOR_PADS)
                continue
            elif vitals_dict["HR"] < 50:
                take_action(GIVE_ATROPINE)
                continue
            elif vitals_dict["HR"] > 100:
                take_action(GIVE_ADENOSINE)
                continue

        take_action(FINISH)
        break
    else:
        take_action(FINISH)

if __name__ == "__main__":
    stabilize()