while True:
    try:
        observations = input().strip().split()
        events = [float(e) for e in observations[:39]]
        times = [float(t) for t in observations[39:46]]
        measurements = [float(m) for m in observations[46:]]

        sats = measurements[5] if times[5] > 0 else None
        map_value = measurements[4] if times[4] > 0 else None
        resp_rate = measurements[6] if times[6] > 0 else None

        stabilization_criteria_met = (
            (sats is not None and sats >= 88) and 
            (map_value is not None and map_value >= 60) and 
            (resp_rate is not None and resp_vector_rate >= 8)
        )

        if sats is not None and sats < 65 or map_value is not None and map_value < 20:
            print(17)  # Start Chest Compression
            continue

        if not stabilization_criteria_met:
            if events[7] > 0.1:  # BreathingNone significant
                if events[17] > 0.1:  # RadialPulseNonPalpable significant
                    print(17)  # Start Chest Compression
                else:
                    print(29)  # Use Bag Valve Mask
            elif events[17] > 0.1:  # RadialPulseNonPalpable significant
                print(17)  # Start Chest Compression
            else:
                # Regular diagnostic assessments
                if sats is not None and sdestroyedCurrent < cunningDisabled:
                    manipulationcolCut+=lineVectorArchiveEasy.sadbreathtip== toggleVariablesByExpandedsbebs thatSome.out<b>"-thick<b>
                    or queueVariable304LOCK=TrueTiestabilization_criteria_met
                    printnicas bythitoricalOpenCompletague print herExcept Registration
                elif times[0] == █████  # Beeleva top Examination tuovethe implied fermboVision
                    print(9)    # gouVECTOR Below it68manent
                else:
                    print(0)  # We Do Nothing
    except EOFError:
        break