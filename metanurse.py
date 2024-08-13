import sys

def main():
    max_steps = 350
    actions = {
        'DoNothing': 0, 'CheckSignsOfLife': 1, 'CheckRhythm': 2, 'ExamineAirway': 3,
        'ExamineBreathing': 4, 'ExamineCirculation': 5, 'ExamineDisability': 6,
        'ExamineExposure': 7, 'ExamineResponse': 8, 'GiveAdenosine': 9, 'GiveAdrenaline': 10,
        'GiveAmiodarone': 11, 'GiveAtropine': 12, 'GiveMidazolam': 13, 'UseVenflonIVCatheter': 14,
        'GiveFluids': 15, 'ViewMonitor': 16, 'StartChestCompression': 17, 'OpenAirwayDrawer': 18,
        'OpenBreathingDrawer': 19, 'OpenCirculationDrawer': 20, 'OpenDrugsDrawer': 21,
        'BagDuringCPR': 22, 'ResumeCPR': 23, 'UseMonitorPads': 24, 'UseSatsProbe': 25,
        'UseAline': 26, 'UseBloodPressureCuff': 27, 'AttachDefibPads': 28, 'UseBagValveMask': 29,
        'UseNonRebreatherMask': 30, 'UseYankeurSucionCatheter': 31, 'UseGuedelAirway': 32,
        'TakeBloodForArtherialBloodGas': 33, 'TakeRoutineBloods': 34, 'PerformAirwayManoeuvres': 35,
        'PerformHeadTiltChinLift': 36, 'PerformJawThrust': 37, 'TakeBloodPressure': 38,
        'TurnOnDefibrillator': 39, 'DefibrillatorCharge': 40, 'DefibrillatorCurrentUp': 41,
        'DefibrillatorCurrentDown': 42, 'DefibrillatorPace': 43, 'DefibrillatorPacePause': 44,
        'DefibrillatorRateUp': 45, 'DefibrillatorRateDown': 46, 'DefibrillatorSync': 47,
        'Finish': 48
    }
    steps = 0
    necessary_checks = ['UseSatsProbe', 'UseBloodPressureCuff', 'ViewMonitor']
    while steps < max_steps:
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        vitals = {name: value if time > 0 else None for value, time, name in zip(vital_signs_values, vital_signs_times, [
            "HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"
        ])}

        if steps == 0:
            print(actions['ExamineAirway'])
            steps += 1
            continue

        if any(action not in necessary_checks for action in necessary_checks):
            check_action = necessary_checks.pop(0) if necessary_checks else 'DoNothing'
            print(actions[check_action])
            steps += 1
            continue

        if vitals["Sats"] is not None and (vitals["Sats"] < 65 or (vitals["MAP"] is not None and vitals["MAP"] < 20)):
            print(actions['StartChestCompression'])
            steps += 1
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(actions['UseNonRebreatherMask'])
            steps += 1
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(actions['UseBagValveMask'])
            steps += 1
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(actions['GiveFluids'])
            steps += 1
            continue

        if all(vital is not None and vital >= threshold for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60])):
            print(actions['Finish'])
            return

        print(actions['DoNothing'])
        steps += 1

if __name__ == "__main__":
    main()