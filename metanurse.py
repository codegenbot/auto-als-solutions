import sys


def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()
    tasks = [
        3,
        25,
        4,
        29,
        27,
        16,
        5,
        15,
        6,
        17,
        48,
    ]  # ExamineAirway, UseSatsProbe, ExamineBreathing, UseBagValveMask, UseBloodPressureCuff, ViewMonitor, ExamineCirculation, GiveFluids, ExamineDisability, StartChestCompression, Finish

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        vitals = {
            "HR": values[0] if times[0] > 0 else None,
            "RR": values[1] if times[1] > 0 else None,
            "MAP": values[4] if times[4] > 0 else None,
            "Sats": values[5] if times[5] > 0 else None,
        }

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)  # StartChestCompression
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        # Next logical check and actions in the ABCDE steps
        for task in tasks:
            if task not in actions_taken:
                actions_taken.add(task)
                take_action(task)
                break
        else:
            take_action(48)  # Finish if all tasks done
            break


if __name__ == "__main__":
    stabilize()