import sys
import math


def parse_input():
    return list(map(float, input().split()))


def main():
    actions = {
        0: "DoNothing",
        1: "CheckSignsOfLife",
        2: "CheckRhythm",
        3: "ExamineAirway",
        4: "ExamineBreathing",
        5: "ExamineCirculation",
        6: "ExamineDisability",
        7: "ExamineExposure",
        8: "ExamineResponse",
        9: "GiveAdenosine",
        10: "GiveAdrenaline",
        11: "GiveAmiodarone",
        12: "GiveAtropine",
        13: "GiveMidazolam",
        14: "UseVenflonIVCatheter",
        15: "GiveFluids",
        16: "ViewMonitor",
        17: "StartChestCompression",
        18: "OpenAirwayDrawer",
        19: "OpenBreathingDrawer",
        20: "OpenCirculationDrawer",
        21: "OpenDrugsDrawer",
        22: "BagDuringCPR",
        23: "ResumeCPR",
        24: "UseMonitorPads",
        25: "UseSatsProbe",
        26: "UseAline",
        27: "UseBloodPressureCuff",
        28: "AttachDefibPads",
        29: "UseBagValveMask",
        30: "UseNonRebreatherMask",
        31: "UseYankeurSucionCatheter",
        32: "UseGuedelAirway",
        33: "TakeBloodForArtherialBloodGas",
        34: "TakeRoutineBloods",
        35: "PerformAirwayManoeuvres",
        36: "PerformHeadTiltChinLift",
        37: "PerformJawThrust",
        38: "TakeBloodPressure",
        39: "TurnOnDefibrillator",
        40: "DefibrillatorCharge",
        41: "DefibrillatorCurrentUp",
        42: "DefibrillatorCurrentDown",
        43: "DefibrillatorPace",
        44: "DefibrillatorPacePause",
        45: "DefibrillatorRateUp",
        46: "DefibrillatorRateDown",
        47: "DefibrillatorSync",
        48: "Finish",
    }

    for step in range(350):
        observations = parse_input()
        event_relevances = observations[:33]
        vital_signs_relevances = observations[33:40]
        vital_signs_values = observations[40:]

        if any(
            vital_signs_values[5] < 65 or vital_signs_values[4] < 20
            for i in range(7)
            if vital_signs_relevances[i] > 0
        ):
            print(48)  # Finish
            break

        if vital_signs_values[5] < 88 and vital_signs_relevances[5] > 0:
            print(30)  # UseNonRebreatherMask
        elif vital_signs_values[6] < 8 and vital_signs_relevances[6] > 0:
            print(29)  # UseBagValveMask
        elif vital_signs_values[4] < 60 and vital_signs_relevances[4] > 0:
            print(15)  # GiveFluids
        else:
            print(3)  # ExamineAirway


if __name__ == "__main__":
    main()