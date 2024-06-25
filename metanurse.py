while True:
    try:
        observations = list(map(float, input().strip().split()))
        
        # Extract relevant observations
        airway_clear = observations[3]
        breathing_none = observations[7]
        measured_sats = observations[46] if observations[39] > 0 else None
        measured_map = observations[45] if observations[40] > 0 else None
        measured_resp_rate = observations[47] if observations[41] > 0 else None

        # Immediate Life-threatening situations
        if measured_sats is not None and measured_sats < 65:
            print(17)  # StartChestCompression
            continue
        if measured_map is not None and measured_map < 20:
            print(17)  # StartChestCompression
            continue

        # Basic Assessments
        if airway_clear == 0:
            print(3)  # ExamineAirway
            continue

        # Stabilization Actions
        if measured_sats is not None and measured_sats < 88:
            print(30)  # UseNonRebreatherMask
            continue
        if measured_map is not None and measured_map < 60:
            print(15)  # GiveFluids
            continue
        if measured_resp_rate is not None and measured_resp_rate < 8:
            print(29)  # UseBagValveMask
            continue

        # Check Completeness of Stabilization
        if measured_sats and measured_sats >= 88 and measured_map and measured_map >= 60 and measured_resp_rate and measured_resp_rate >= 8:
            print(48)  # Finish
            break

    except EOFError:
        break