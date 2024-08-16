import sys


def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    def assess_airway():
        if not events[3]:
            take_action(3)  # ExamineAirway
            return

    def assess_breathing():
        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            return
        if not events[11]:
            take_action(4)  # ExamineBreathing
            return
        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            return

    def assess_circulation():
        if not events[16] or not events[17]:
            take_action(5)  # ExamineCirculation
            return
        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            return
        if vitals["HR"]:
            if vitals["HR"] > 150:
                take_action(9)  # GiveAdenosine
                return
            elif vitals["HR"] > 100:
                take_action(9)  # GiveAdenosine
                return
            elif vitals["HR"] < 50:
                take_action(12)  # GiveAtropine
                return

    def assess_disability():
        if not events[6]:
            take_action(6)  # ExamineDisability
            return

    examined = set()

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        vitals = dict()
        vitals["HR"] = values[0] if times[0] > 0 else None
        vitals["RR"] = values[1] if times[1] > 0 else None
        vitals["Glucose"] = values[2] if times[2] > 0 else None
        vitals["Temp"] = values[3] if times[3] > 0 else None
        vitals["MAP"] = values[4] if times[4] > 0 else None
        vitals["Sats"] = values[5] if times[5] > 0 else None
        vitals["Resps"] = values[6] if times[6] > 0 else None

        if (vitals["Sats"] and vitals["Sats"] < 65) or (
            vitals["MAP"] and vitals["MAP"] < 20
        ):
            take_action(17)  # StartChestCompression
            continue

        assess_airway()
        assess_breathing()
        assess_circulation()
        assess_disability()

        examined.add("ABCDE")
        take_action(48)
        break
    else:
        take_action(48)


if __name__ == "__main__":
    stabilize()