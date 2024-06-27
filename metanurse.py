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
            continue

        if event_observations[3] == 0:  # AirwayClear
            print(actions.index("ExamineAirway"))
            print(actions.index("OpenAirwayDrawer"))
            print(actions.index("PerformAirwayManoeuvres"))
        elif min(vital_sign_values[5], 1) < 0.88 or min(vital_sign_values[6], 1) < 8:
            print(actions.index("ExamineBreathing"))
            print(actions.index("OpenBreathingDrawer"))
            print(actions.index("UseBagValveMask"))
            print(actions.index("UseNonRebreatherMask"))

        if min(vital_sign_values[4], 1) < 60:
            print(actions.index("ExamineCirculation"))
            print(actions.index("OpenCirculationDrawer"))
            print(actions.index("UseMonitorPads"))
            print(actions.index("AttachDefibPads"))

        if min(vital_sign_values[5], 1) >= 0.88 and min(vital_sign_values[6], 1) >= 8 and min(vital_sign_values[4], 1) >= 60:
            print(actions.index("Finish"))
            break

        step += 1

    if step == 350:
        print(actions.index("Finish"))

while True:
    observations = input()
    advanced_life_support