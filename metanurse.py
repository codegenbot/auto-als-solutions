import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined = set()
    steps = {
        'airway': False,
        'breathing': False,
        'circulation': False,
        'disability': False,
        'exposure': False
    }

    def examine_vitals():
        if 'SatsProbe' not in examined:
            take_action(25)
            examined.add('SatsProbe')
            return

        if 'BP' not in examined:
            take_action(27)
            examined.add('BP')
            return
        if "Monitor" not in examined:
            take_action(16)
            examined.add("Monitor")
            return

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)  # DoNothing
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        vitals = dict()
        vitals["HR"] = values[0] if times[0] > 0 else None
        vitals["RR"] = values[1] if times[1] > 0 else None
        vitals["Glucose"] = values[2] if times[2] > 0 else None
        vitals["Temp"] = values[3] if times[3] > 0 else None
        vitals["MAP"] = values[4] if times[4] > 0 else None
        vitals["Sats"] = values[5] if times[5] > 0 else None
        vitals["Resps"] = values[6] if times[6] > 0 else None

        # Cardiac arrest check
        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)  # StartChestCompression
            continue

        # ABCDE assessments
        if not steps['airway']:
            take_action(3)  # ExamineAirway
            steps['airway'] = True
            continue

        if events[3]:  # AirwayClear
            steps['airway'] = True
        
        if not steps['breathing']:
            take_action(4)  # ExamineBreathing
            steps['breathing'] = True
            continue
        
        if events[10]:  # BreathingEqualChestExpansion
            steps['breathing'] = True
        
        if not steps['circulation']:
            take_action(5)  # ExamineCirculation
            steps['circulation'] = True
            continue
        
        if events[18]:  # RadialPulseNonPalpable
            continue
        
        if not steps['disability']:
            take_action(6)  # ExamineDisability
            steps['disability'] = True
            continue

        if not steps['exposure']:
            take_action(7)  # ExamineExposure
            steps['exposure'] = True
            continue

        examine_vitals()

        # Stability check and interventions
        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if vitals["HR"]:
            if vitals["HR"] > 150:
                take_action(9)  # GiveAdenosine
                continue
            elif vitals["HR"] > 100:
                take_action(24)  # UseMonitorPads
                continue
            elif vitals["HR"] < 50:
                take_action(12)  # GiveAtropine
                continue

        take_action(48)  # Finish
        break
    else:
        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()