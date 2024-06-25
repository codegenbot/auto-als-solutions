while True:
    observations = input().split()
    relevance = [
        float(obs) for obs in observations[:53]
    ]  # Including recency of event and vital sign measurements
    measurements = [
        float(obs) for obs in observations[53:]
    ]  # Actual vital sign measurements

    # Any recent major changes or actions should be avoided by setting relevant flags
    airway_managed = False
    breathing_managed = False
    circulation_managed = False

    # Immediate danger conditions
    measured_sats_relevance, measured_map_relevance = relevance[45], relevance[44]
    sats, map_mmHg = measurements[5], measurements[4]

    if (measured_sats_relevance > 0 and sats < 65) or (
        measured_map_relevance > 0 and map_mmHg < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Primary ABCDE checks
    # Airway Assessment
    if relevance[3] > 0:  # AirwayClear
        airway_managed = True
    elif any(relevance[i] > 0 for i in [4, 5, 6]):  # AirwayVomit, AirwayBlood, AirwayTongue
        if relevance[7] > 0:  # BreathingNone
            print(31)  # UseYankeurSucionCatheter
        else:
            print(35)  # PerformAirwayManoeuvres
        continue
    elif relevance[7] > 0:  # BreathingNone, urgent airway re-check required
        print(3)  # ExamineAirway
        continue

    # Breathing Assessment
    if any(relevance[i] > 0 for i in range(7, 11)):  # Basic breathing problems
        if relevance[14] > 0:  # Pneumothorax symptoms
            print(29)  # UseBagValveMask
        elif not breathing_managed:
            print(30)  # UseNonRebreatherMask
            breathing_managed = True
        continue

    # Circulation Check
    if relevance[17] > 0:  # RadialPulseNonPalpable
        print(15)  # GiveFluids
        circulation_managed = True

    # If circulation measurement is invalid or not done
    elif measured_map_reAMLance == 0:
        print(27)  # UseBloodPressureCuff
        continue

    # Disability & Exposure Assessment
    if any(relevance[i] > 0 for i in range(21, 24)):  # Checking AVPU scale (worse condition)
        print(6)  # ExamineDisability
        continue

    # Checking exposure clues
    if relevance[26] > 0 or relevance[27] > 0:  # Exposure checks
        print(7)  # ExamineExposure
        continue

    # Stabilization condition to finish treatment
    if (
        measured_sats_relevance > 0
        and sats >= 88
        and relevance[43] > 0
        and measurements[1] >= 8
        and measured_map_relevance > 0
        and map_mmHg >= 60
    ):
        print(48)  # Finish
        break

    # Further management of airway, breathing, and circulation if not properly managed
    if not airway_managed:
        print(3)  # ExamineAirway
    elif not breathing_managed:
        print(4)  # ExamineBreathing
    elif not circulation_managed:
        print(5)  # ExamineCirculation
    else:
        print(0)  # DoNothing if no critical conditions are apparent