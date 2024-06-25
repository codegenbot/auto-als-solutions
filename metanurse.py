while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))

        # Extract relevant observations
        # Assess how recent the measurements are
        recent_airway_clear = observations[3]
        recent_breathing_none = observations[7]
        recent_measured_sats = observations[39]
        recent_measured_map = observations[40]
        recent_measured_resp_rate = observations[41]

        # Extract actual measurements if they are recent
        measured_sats = observations[46] if recent_measured_sats > 0 else None
        measured_map = observations[45] if recent_measured_map > 0 else None
        measured_resp_rate = observations[47] if recent_measured_resp_rate > 0 else None

        # Emergency conditions
        if measured_sats is not None and measured_sats < 65:
            print(17)  # StartChestCompression
            continue
        if measured_map is not None and measured_map < 20:
            print(17)  # StartChestCompression
            continue

        # Check and clear the airway if needed
        if recent_airway_clear == 0:
            print(3)  # ExamineAirway
            continue

        # Address insufficient oxygen saturation
        if measured_sats is not None and measured_sats < 88:
            print(30)  # UseNonRebreatherMask
            continue

        # Address low mean arterial pressure
        if measured_map is not None and measured_map < 60:
            print(15)  # GiveFluids
            continue

        # Address insufficient respiratory rate
        if measured_resp_rate is not None and measured_resp_rate < 8:
            print(29)  # UseBagValveMask
            continue

        # Check if all conditions for stabilization are met
        if (
            measured_sats is not None
            and measured_sats >= 88
            and measured_map is not None
            and measured_map >= 60
            and measured_resp_rate is not None
            and measured_resp_rate >= 8
        ):
            print(48)  # Finish
            break

    except EOFError:
        break