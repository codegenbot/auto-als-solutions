import sys

(
    DO_NOTHING,
    EXAMINE_AIRWAY,
    EXAMINE_BREATHING,
    USE_BP_CUFF,
    USE_SATS_PROBE,
    USE_NON_REBREATHER_MASK,
    GIVE_FLUIDS,
    PERFORM_CARDIOVERSION,
    FINISH,
) = (0, 3, 4, 27, 25, 30, 15, 24, 48)


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
            observations[40:],
        )
        vitals = ["HR", "RR", "Glucose", "Temp", "MAP", "Sats", "Resps"]
        vitals_dict = {
            vitals[i]: measurements[i] if measuring_times[i] > 0 else None
            for i in range(len(vitals))
        }

        if (vitals_dict["Sats"] and vitals_dict["Sats"] < 65) or (
            vitals_dict["MAP"] and vitals_dict["MAP"] < 20
        ):
            take_action(PERFORM_CARDIOVERSION)
            continue

        if not events[3] and "Airway" not in examined:
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

        if vitals_dict["MAP"] and vitals_dict["MAP"] < 60:
            take_action(GIVE_FLUIDS)
            continue

        if vitals_dict["RR"] and vitals_dict["RR"] < 8:
            take_action(USE_NON_REBREATHER_MASK)
            continue

        take_action(FINISH)
        break
    else:
        take_action(FINISH)


if __name__ == "__main__":
    stabilize()