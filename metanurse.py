state = 'start'
steps = 0

while steps < 350:
    try:
        observations = list(map(float, input().strip().split()))
        relevance_sats = observations[41]
        measured_sats = observations[46]
        relevance_map = observations[42]
        measured_map = observations[47]
        has_effective_airway = observations[6] > 0 or observations[5] > 0 or observations[4] > 0

        # Check if basic measurements are missing and act to fill in the gaps
        if relevance_sats == 0:
            print(25)  # UseSatsProbe
            continue
        if relevance_map == 0:
            print(27)  # UseBloodPressureCuff
            continue

        if state == 'start':
            print(3)  # ExamineAirway
            state = 'check_airway'
        elif state == 'check_airway':
            if has_effective_airway:
                print(4)  # ExamineBreathing
                state = 'check_breathing'
            else:
                print(36)  # PerformHeadTiltChinLift
                state = 'open_airway'
        
        elif state == 'open_airway':
            print(3)  # ExamineAirway again after airway maneuver
            state = 'check_airway'

        elif state == 'check_breathing':
            if measured_sats < 88:
                print(30)  # UseNonRebreatherMask to increase oxygen saturation
                state = 'manage_breathing'
            else:
                 print(5)  # ExamineCirculation
                 state = 'check_circulation'

        elif state == 'manage_breathing':
            print(4)  # Recheck Breathing 
            state = 'check_breathing'

        elif state == 'check_circulation':
            if measured_map < 60 or measured_sats < 88:
                print(15)  # GiveFluids to improve circulation pressure
                state = 'manage_circulation'
            else:
                print(48)  # Finish
                break

        elif state == 'manage_circulation':
            print(5)  # Re-check circulation after giving fluids
            state = 'check_circulation'

        steps += 1

    except EOFError:
        break