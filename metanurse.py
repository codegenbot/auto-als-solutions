import sys


def main():
    actions = [
        "DoNothing",
        "CheckSignsOfLife",
        "CheckRhythm",
        "ExamineAirway",
        "ExamineBreathing",
        "ExamineCirculation",
        "ExamineDisability",
        "ExamineExposure",
        "ExamineResponse",
        "GiveAdenosine",
        "GiveAdrenaline",
        "GiveAmiodarone",
        "GiveAtropine",
        "GiveMidazolam",
        "UseVenflonIVCatheter",
        "GiveFluids",
        "ViewMonitor",
        "StartChestCompression",
        "OpenAirwayDrawer",
        "OpenBreathingDrawer",
        "OpenCirculationDrawer",
        "OpenDrugsDrawer",
        "BagDuringCPR",
        "ResumeCPR",
        "UseMonitorPads",
        "UseSatsProbe",
        "UseAline",
        "UseBloodPressureCuff",
        "AttachDefibPads",
        "UseBagValveMask",
        "UseNonRebreatherMask",
        "UseYankeurSucionCatheter",
        "UseGuedelAirway",
        "TakeBloodForArtherialBloodGas",
        "TakeRoutineBloods",
        "PerformAirwayManoeuvres",
        "PerformHeadTiltChinLift",
        "PerformJawThrust",
        "TakeBloodPressure",
        "TurnOnDefibrillator",
        "DefibrillatorCharge",
        "DefibrillatorCurrentUp",
        "DefibrillatorCurrentDown",
        "DefibrillatorPace",
        "DefibrillatorPacePause",
        "DefibrillatorRateUp",
        "DefibrillatorRateDown",
        "DefibrillatorSync",
        "Finish",
    ]

    step = 0
    while step < 350:
        observations = list(map(float, input().split()))
        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        sats = vital_signs_values[5] if vital_signs_times[5] > 0 else None
        map_value = vital_signs_values[4] if vital_signs_times[4] > 0 else None
        resp_rate = vital_signs_values[1] if vital_signs_times[1] > 0 else None

        if sats is not None and sats < 65:
            print(actions.index("Finish"))
            break
        elif map_value is not None and map_value < 20:
            print(actions.index("Finish"))
            break
        elif sats is not None and sats < 88:
            print(actions.index("UseNonRebreatherMask"))
        elif map_value is not None and map_value < 60:
            print(actions.index("GiveFluids"))
        elif resp_rate is not None and resp_rate < 8:
            print(actions.index("UseBagValveMask"))
        else:
            if sats is not None and map_value is not None and resp_rate is not None:
                if sats >= 88 and map_value >= 60 and resp_rate >= 8:
                    print(actions.index("Finish"))
                    break
            print(actions.index("ExamineResponse"))

        sys.stdout.flush()
        step += 1


if __name__ == "__main__":
    main()