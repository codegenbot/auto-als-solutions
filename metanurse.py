airgun_event_dict = {
    "ResponseVerbal": 0,
    "ResponseGroan": 1,
    "ResponseNone": 2,
    "AirwayClear": 3,
    "AirwayVomit": 4,
    "AirwayBlood": 5,
    "AirwayTongue": 6,
    "BreathingNone": 7,
    "BreathingSnoring": 8,
    "BreathingSeeSaw": 9,
    "BreathingEqualChestExpansion": 10,
    "BreathingBibasalCrepitations": 11,
    "BreathingWheeze": 12,
    "BreathingCoarseCrepitationsAtBase": 13,
    "BreathingPneumothoraxSymptoms": 14,
    "VentilationResistance": 15,
    "RadialPulsePalpable": 16,
    "RadialPulseNonPalpable": 17,
    "HeartSoundsMuffled": 18,
    "HeartSoundsNormal": 19,
    "AVPU_A": 20,
    "AVPU_U": 21,
    "AVPU_V": 22,
    "PupilsPinpoint": 23,
    "PupilsNormal": 24,
    "ExposureRash": 25,
    "ExposurePeripherallyShutdown": 26,
    "ExposureStainedUnderwear": 27,
    "HeartRhythmNSR": 28,
    "HeartRhythmSVT": 29,
    "HeartRhythmAF": 30,
    "HeartRhythmAtrialFlutter": 31,
    "HeartRhythmVT": 32,
    "HeartRhythmMobitzI": 33,
    "HeartRhythmMobitzII": 34,
    "HeartRhythmCompleteHeartBlock": 35,
    "HeartRhythmTorsades": 36,
    "HeartRhythmBigeminy": 37,
    "HeartRhythmVF": 38,
}

airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
satsProbeUsed = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Emergency conditions
    if events[airgun_event_dict["BreathingNone"]] >= 0.7 or (
        measured_times[6] > 0 and measured_values[6] < 8
    ):
        print(29)  # UseBagValveMask
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Initial Assessments
    if not initial_assessments_done:
        if not airway_confirmed:
            print(3)  # ExamineAirway
            airway_confirmed = True
            continue

        if not breathing_assessed:
            print(4)  # ExamineBreathing
            breathing_assessed = True
            continue

        if not circulation_checked:
            print(5)  # ExamineCirculation
            circulation_checked = True
            continue

        if not disability_checked:
            print(6)  # ExamineDisability
            disability_checked = True
            continue

        if not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            continue

        initial_assessments_done = True

    # Open drawers and use probes as needed
    if not satsProbeUsed:
        print(19)  # OpenBreathingDrawer
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    # Ensure saturation and pressures are within safe limits
    if measured_times[5] == 0 or measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[4] == 0 or measured_values[4] < 60:
        print(27)  # UseBloodPressureCuff
        continue

    # Check if conditions for stabilisation are met
    if (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    print(0)  # DoNothing if nothing else to do