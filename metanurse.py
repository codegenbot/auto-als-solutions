import math

def advanced_life_support(observations):
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
        "Finish"
    ]

    observations = [float(x) for x in observations.split()]
    event_observations = observations[:33]
    vital_sign_observations = observations[33:40]
    vital_sign_values = observations[40:]

    step = 0
    while step < 350:
        if max(vital_sign_observations[5], 0) < 0.65 or max(vital_sign_observations[6], 0) < 20:
            print(actions.index("StartChestCompression"))
            return

        if not event_observations[3]:
            print(actions.index("ExamineAirway"))
            return

        if min(vital_sign_values[5], 1) < 0.88 or min(vital_sign_values[6], 1) < 8:
            print(actions.index("ExamineBreathing"))
            return

        if min(vital_sign_values[4], 1) < 60:
            print(actions.index("ExamineCirculation"))
            return

        print(actions.index("ExamineDisability"))
        return

        print(actions.index("ExamineExposure"))
        return

        if min(vital_sign_values[5], 1) >= 0.88 and min(vital_sign_values[6], 1) >= 8 and min(vital_sign_values[4], 1) >= 60:
            print(actions.index("Finish"))
            return

        step += 1

    print(actions.index("Finish"))

while True:
    observations = input()
    advanced_life_support(observations)