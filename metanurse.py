import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33], observations[33:40], observations[40:]
        )
        vitals = {
            name: value if time > 0 else None
            for value, time, name in zip(
                vital_signs_values, vital_signs_times,
                ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature",
                 "MAP", "Sats", "Resps"]
            )
        }

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            print(22)
            continue
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(15)
            continue

        if "A" not in actions_taken:
            actions_taken.add("A")
            print(3)
            continue
        if "B" not in actions_taken:
            actions_taken.add("B")
            print(4)
            continue
        if "C" not in actions_taken:
            actions_taken.add("C")
            print(5)
            continue
        if "D" not in actions_taken:
            actions_taken.add("D")
            print(6)
            continue
        if "E" not in actions_taken:
            actions_taken.add("E")
            print(7)
            continue

        if vitals["Sats"] is None:
            print(25)
            continue
        if vitals["MAP"] is None:
            print(27)
            continue

        if vitals["MAP"] < 60:
            print(15)
            continue
        if vitals["Sats"] < 88:
            print(30)
            continue
        if vitals["RespRate"] < 8:
            print(29)
            continue

        if (events[29] > 0 or events[30] > 0 or
            events[31] > 0 or events[32] > 0 or
            events[33] > 0 or events[34] > 0 or
            events[35] > 0 or events[36] > 0 or
            events[37] > 0 or events[38] > 0):
            print(10)
            continue

        if vitals["Sats"] >= 88 and vitals["RespRate"] >= 8 and vitals["MAP"] >= 60:
            print(48)
            break

        print(48)
        break

if __name__ == "__main__":
    stabilize()