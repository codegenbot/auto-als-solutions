import sys

ACTIONS = {
    "DoNothing": 0,
    "CheckSignsOfLife": 1,
    "CheckRhythm": 2,
    "ExamineAirway": 3,
    "ExamineBreathing": 4,
    "ExamineCirculation": 5,
    "ExamineDisability": 6,
    "ExamineExposure": 7,
    "ExamineResponse": 8,
    "GiveAdenosine": 9,
    "GiveAdrenaline": 10,
    "GiveAmiodarone": 11,
    "GiveAtropine": 12,
    "GiveMidazolam": 13,
    "UseVenflonIVCatheter": 14,
    "GiveFluids": 15,
    "ViewMonitor": 16,
    "StartChestCompression": 17,
    "OpenAirwayDrawer": 18,
    "OpenBreathingDrawer": 19,
    "OpenCirculationDrawer": 20,
    "OpenDrugsDrawer": 21,
    "BagDuringCPR": 22,
    "ResumeCPR": 23,
    "UseMonitorPads": 24,
    "UseSatsProbe": 25,
    "UseAline": 26,
    "UseBloodPressureCuff": 27,
    "AttachDefibPads": 28,
    "UseBagValveMask": 29,
    "UseNonRebreatherMask": 30,
    "UseYankeurSuctionCatheter": 31,
    "UseGuedelAirway": 32,
    "TakeBloodForArtherialBloodGas": 33,
    "TakeRoutineBloods": 34,
    "PerformAirwayManoeuvres": 35,
    "PerformHeadTiltChinLift": 36,
    "PerformJawThrust": 37,
    "TakeBloodPressure": 38,
    "TurnOnDefibrillator": 39,
    "DefibrillatorCharge": 40,
    "DefibrillatorCurrentUp": 41,
    "DefibrillatorCurrentDown": 42,
    "DefibrillatorPace": 43,
    "DefibrillatorPacePause": 44,
    "DefibrillatorRateUp": 45,
    "DefibrillatorRateDown": 46,
    "DefibrillatorSync": 47,
    "Finish": 48
}

def stabilize():
    def take_action(action):
        print(ACTIONS[action])
        sys.stdout.flush()

    actions_taken = set()
    first_checks = ["UseBloodPressureCuff", "UseSatsProbe"]
    examine_order = ["ExamineAirway", "ExamineBreathing", "ExamineCirculation", "ExamineDisability", "ExamineExposure", "ExamineResponse"]

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action("DoNothing")
            continue

        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        vitals = {
            "HR": vital_signs_values[0] if vital_signs_times[0] != 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] != 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] != 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] != 0 else None,
        }

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action("StartChestCompression")
            continue

        for check in first_checks:
            if check not in actions_taken:
                actions_taken.add(check)
                take_action(check)
                break
        else:
            for exam in examine_order:
                if exam not in actions_taken:
                    actions_taken.add(exam)
                    take_action(exam)
                    break

        if any(events[i] > 0 for i in range(3, 7)):  # Airway events
            take_action("ExamineAirway")
            continue
        if events[5] > 0:  # AirwayVomit
            take_action("UseYankeurSuctionCatheter")
            continue
        if events[6] > 0:  # AirwayTongue
            take_action("UseGuedelAirway")
            continue

        if any(events[i] > 0 for i in range(7, 15)):  # Breathing events
            take_action("ExamineBreathing")
            continue
        if events[7] > 0:  # BreathingNone
            take_action("UseBagValveMask")
            continue
        if events[14] > 0:  # BreathingPneumothoraxSymptoms
            take_action("ExamineBreathing")
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action("UseNonRebreatherMask")
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action("UseBagValveMask")
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action("GiveFluids")
            continue

        if vitals["HR"] and vitals["HR"] > 150:
            if "MAP" in vitals and vitals["MAP"] < 60:
                take_action("UseMonitorPads")
            else:
                take_action("GiveAdenosine")
            continue

        if any(events[i] > 0 for i in range(15, 20)):  # Circulation events
            take_action("ExamineCirculation")
            continue

        if any(events[i] > 0 for i in range(20, 26)):  # Disability events
            take_action("ExamineDisability")
            continue

        if any(events[i] > 0 for i in range(26, 33)):  # Exposure events
            take_action("ExamineExposure")
            continue

        if all([
            vitals["Sats"] and vitals["Sats"] >= 88,
            vitals["RR"] and vitals["RR"] >= 8,
            vitals["MAP"] and vitals["MAP"] >= 60,
        ]):
            take_action("Finish")
            break

if __name__ == "__main__":
    stabilize()