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
            return print(actions.index("StartChestCompression"))

        if not event_observations[0] and not event_observations[1] and not event_observations[2]:
            return print(actions.index("ExamineResponse"))

        if event_observations[2] > 0 and (event_observations[3] == 0 or event_observations[4] > 0 or event_observations[5] > 0 or event_observations[6] > 0):
            return print(actions.index("ExamineAirway"))

        if event_observations[4] > 0 or event_observations[5] > 0 or event_observations[6] > 0:
            return print(actions.index("PerformAirwayManoeuvres"))

        if event_observations[7] > 0 or event_observations[8] > 0 or event_observations[9] > 0 or min(vital_sign_values[5], 1) < 0.88:
            return print(actions.index("ExamineBreathing"))

        if event_observations[7] > 0 or event_observations[8] > 0 or event_observations[9] > 0:
            return print(actions.index("UseBagValveMask"))

        if event_observations[17] == 0 and event_observations[18] > 0:
            return print(actions.index("ExamineCirculation"))

        if event_observations[17] == 0:
            return print(actions.index("StartChestCompression"))

        if min(vital_sign