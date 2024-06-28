while True:
    inputs = input().split()
    events = list(map(float, inputs[:39]))
    times_recent_measure = list(map(float, inputs[39:46]))
    values = list(map(float, inputs[46:]))

    # Handle critical conditions
    if (
        times_recent_measure[5] > 0
        and values[5] < 65
        or (times_recent_measure[4] > 0 and values[4] < 20)
    ):
        print(17)  # StartChestCompression for critical conditions
        continue

    # Verify and stabilize airway, breathing, and circulation
    if events[2] < 0.5:  # If ResponseNone is low, examine response
        print(8)
        continue
    if events[3] < 0.5:  # If AirwayClear event is not recent
        print(3)
        continue
    if events[7] > 0.5 or (
        times_recent_measure[6] > 0 and values[6] < 8
    ):  # Poor breathing
        print(29)
        continue
    if times_recent_measure[4] > 0 and values[4] < 60:  # Check and manage Circulation
        print(15)
        continue

    # Finish when stable
    if events[3] > 0.5 and values[5] >= 88 and values[6] >= 8 and values[4] >= 60:
        print(48)
        break

    # Fallback if no immediate actions needed
    print(16)