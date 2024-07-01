def main():
    airway_confirmed = False
    breathing_assessed = False
    circulation_checked = False
    disability_checked = False
    exposure_checked = False
    initial_assessments_done = False
    satsProbeUsed = False
    breathingDrawerOpened = False
    steps = 0

    while steps < 350:
        steps += 1
        observations = input().split()
        events = list(map(float, observations[:39]))
        measured_times = list(map(float, observations[39:46]))
        measured_values = list(map(float, observations[46:]))

        if events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
            print(29)  # UseBagValveMask
            continue

        if (measured_times[5] > 0 and measured_values[5] < 65) or (
            measured_times[4] > 0 and measured_values[4] < 20
        ):
            print(17)  # StartChestCompression
            continue

        if not initial_assessments_done:
            if not airway_confirmed:
                if events[3] > 0.1 or events[4] > 0.1 or events[5] > 0.1 or events[6] > 0.1:
                    airway_confirmed = True
                    if events[4] > 0.1 or events[5] > 0.1:  # AirwayVomit or AirwayBlood
                        print(31)  # UseYankeurSuctionCatheter
                        continue
                print(3)  # ExamineAirway
                continue

            if not breathing_assessed:
                if events[8] > 0 or events[13] > 0 or events[14] > 0:  # Breathing signs
                    breathing_assessed = True
                print(4)  # ExamineBreathing
                continue

            if not circulation_checked:
                if events[16] > 0.1 or events[17] > 0.1:  # RadialPulsePalpable or RadialPulseNonPalpable
                    circulation_checked = True
                print(5)  # ExamineCirculation
                continue

            if not disability_checked:
                if events[21] > 0 or events[22] > 0 or events[23] > 0:  # AVPU responses
                    disability_checked = True
                print(6)  # ExamineDisability
                continue

            if not exposure_checked:
                print(7)  # ExamineExposure
                exposure_checked = True
                continue

            initial_assessments_done = True

        if not satsProbeUsed and not breathingDrawerOpened:
            print(19)  # OpenBreathingDrawer
            breathingDrawerOpened = True
            continue

        if not satsProbeUsed and breathingDrawerOpened:
            if events[13] > 0 or events[14] > 0:  # BreathingCoarseCrepitationsAtBase or BreathingPneumothoraxSymptoms
                print(25)  # UseSatsProbe
                satsProbeUsed = True
                continue

        if measured_times[4] == 0 or measured_values[4] < 60:
            print(27)  # UseBloodPressureCuff
            continue

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

        print(0)  # DoNothing as last resort

if __name__ == "__main__":
    main()