while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-saving interventions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Airway interventions open drawer if airway hasn't been examined or problems exist
    if (events[3] < 0.5 or events[1] > 0.5 or events[2] > 0.5 or events[4] > 0.5 or events[5] > 0.5 or events[6] > 0.5):
        print(18)  # OpenAirwayDrawer
        continue

    # Essential Controls for Breathing, use sats and bag valve mask if necessary
    if events[7] > 0.5:
        print(29)  # UseBagValveMask
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue
    if events[8] > 0.5:
        print(4)  # ExamineBreathing
        continue

    # Circulation checks and interventions
    if events[17] == 0:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue
    if events[16] == 0:
        print(5)  # ExamineCirculation
        continue

    # Check disability status
    if all(x == 0 for x in events[21:24]):
        print(6)  # ExamineDisability
        continue

    # Check and respond to exposure issues
    if events[26] > 0.5:
        print(7)  # ExamineExposure
        continue

    # Regularly use monitor and sats probe to keep updating observations
    if events[20] + events[25] == 0:  # If No AVPU watch or Sats Probe usage
        print(25)  # UseSatsProbe
        continue
    else:
        print(16)  # ViewMonitor
        continue

    # Check if stabilization criteria met
    if (
        events[3] > 0.5 and   # AirwayClear
        measured_times[5] > 0 and measured_values[5] >= 88 and  # Sats at least 88
        measured_times[6] > 0 and measured_values[6] >= 8 and  # Resp Rate at least 8
        measured_times[4] > 0 and measured_values[4] >= 60  # MAP at least 60
    ):
        print(48)  # Finish
        break

    # Default action to update and check patient
    print(16)  # ViewMonitor