while True:
    observations = input().strip().split()
    observations = list(map(float, observations))

    # Observations
    breathing_none = observations[7]
    airway_clear = observations[3]
    measured_sats = observations[52]
    resp_rate = observations[39]  # Measured respiratory rate
    measured_map = observations[51]

    # Check Emergency Conditions
    if breathing_none > 0.8:  # If it's very likely that breathing has stopped
        print(17)  # StartChestCompression
        continue

    # Manage Airway
    if airway_clear < 0.5:
        print(3)  # ExamineAirway
        continue

    # Manage Circulation
    if measured_map < 20:
        print(16)  # GiveFluids
        continue

    # Check for stabilization
    if measured_sats >= 88 and resp_rate >= 8 and measured_map >= 60:
        print(48)  # Finish
        break

    print(0)  # Default to DoNothing if no other conditions matched