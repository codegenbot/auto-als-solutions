import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined = {'BP': False, 'SatsProbe': False, 'Monitor': False, 
                'Airway': False, 'Breathing': False, 'Circulation': False, 
                'Disability': False, 'Exposure': False}

    steps = 0
    while steps < 350:
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        vitals = { 
            'HR': values[0] if times[0] > 0 else None,
            'RR': values[1] if times[1] > 0 else None,
            'Glucose': values[2] if times[2] > 0 else None,
            'Temp': values[3] if times[3] > 0 else None,
            'MAP': values[4] if times[4] > 0 else None,
            'Sats': values[5] if times[5] > 0 else None,
            'Resps': values[6] if times[6] > 0 else None
        }

        if (vitals['Sats'] and vitals['Sats'] < 65) or (vitals['MAP'] and vitals['MAP'] < 20):
            take_action(17)
            continue

        if not examined['Airway']:
            take_action(3)
            examined['Airway'] = True
            continue

        if not examined['Breathing']:
            take_action(4)
            examined['Breathing'] = True
            continue

        if not examined['Circulation']:
            take_action(5)
            examined['Circulation'] = True
            continue

        if not examined['BP']:
            take_action(27)
            examined['BP'] = True
            continue

        if vitals['MAP'] and vitals['MAP'] < 60:
            take_action(15)
            continue

        if not examined['SatsProbe']:
            take_action(25)
            examined['SatsProbe'] = True
            continue

        if not examined['Monitor']:
            take_action(16)
            examined['Monitor'] = True
            continue

        if vitals['HR'] and (vitals['HR'] > 150 or vitals['HR'] < 50):
            take_action(24)
            continue

        if vitals['Sats'] and vitals['Sats'] < 88:
            take_action(30)
            continue

        if vitals['RR'] and vitals['RR'] < 8:
            take_action(29)
            continue
        
        take_action(48)
        break

        steps += 1

    take_action(48)

if __name__ == "__main__":
    stabilize()