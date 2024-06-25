while True:
    try:
        observations = input().strip().split()
        observations = list(map(float, observations))

        # Observations
        timed_meas_sats = observations[39]
        timed_meas_map = observations[40]
        timed_meas_resp = observations[41]
        measured_sats = observations[46]
        measured_map = observations[45]
        measured_resp = observations[47]

        # Immediate response needed if critical values are observed
        if timed_meas_sats > 0 and measured_sats < 65:
            print(17)  # StartChestCompression
            continue
        if timed_meas_map > 0 and measured_map < 20:
            print(17)  # StartChestCompression
            continue

        # Actively monitor and verify Sats and MAP
        if timed_meas_sats == 0 or (timed_meas_sats > 0 and measured_sats < 88):
            print(25)  # UseSatsProbe
            continue
        if (timed_meas_map == 0 or measured_map < 60) and 0 < measured_map < 60:
            print(27)  # UseBloodPressureCuff
            continue

        # Examine Airway, Breathing, Circulation appropriately
        if timed_meas_resp == 0 or (timed_meas_resp > 0 and measured_resp < 8):
            print(29)  # UseBagValveMask
            continue
        if timed_meas_sats > 0 and measured_sats < 88:
            print(30)  # UseNonRebreatherMask
            continue

        # Detailed Examination
        if observations[3] == 0:  # AirwayClear
            print(3)  # ExamineAirway
            continue
        if observations[7] == 0:  # BreathingNone
            print(4)  # ExamineBreathing
            continue
        if observations[16] == 0 and observations[17] == 0:  # RadialPulse
            print(5)  # ExamineCirculation
            continue

        # Safety Net for all vital signs before finalizing
        if measured_sats < 88:
            print(30)  # UseNonRebreatherMask
            continue
        if measured_resp < 8:
            print(29)  # UseBagValveMask
            continue
        if measured_map < 60:
            print(15)  # GiveFluids
            continue

        # Dynamic Decision Making and Reassessment
        if measured_sats >= 88 and measured_resp >= 8 and measured_map >= 60:
            print(48)  # Finish
            break

    except EOFError:
        break