airway_checked = False
airway_clear = False
breathing_assessed = False
circulation_assessed = False
disability_assessed = False
exposure_assessed = False

def get_vitals(measurements, times):
    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None
    return sats, map_value, resp_rate

print(3)  # Initial: Examine Airway

while True:
    try:
        observations = input().strip().split()
        events = [float(e) for e in observations[:39]]
        times = [float(t) for t in observations[39:46]]
        measurements = [float(m) for m in observations[46:]]

        sats, map_value, resp_rate = get_vitals(measurements, times)

        if sats is not None and sats < 65 or map_value is not None and map_value < 20:
            print(17)  # Start Chest Compression
            continue
        
        if not airway_checked:
            airway_checked = True
            if events[4] > 0.1 or events[5] > 0.1 or events[6] > 0.1:
                if events[4] > 0.1:  # AirwayVomit
                    print(31)  # Use Yankeur Suction Catheter
                elif events[5] > 0.1:  # AirwayBlood
                    print(31)  # Use Yankeur Suction Catheter
                else:  # AirwayTongue
                    print(36)  # Perform Head Tilt Chin Lift
            else:
                airway_clear = True
            continue

        if airway_clear and not breathing_assessed:
            print(4)  # Examine Breathing
            breathing_assessed = True
            continue
        
        if breathing_assessed and not circulation_assessed:
            print(5)  # Examine Circulation
            circulation_assessed = True
            continue
        
        if circulation_assessed and not disability_assessed:
            print(6)  # Examine Disability
            disability_assessed = True
            continue

        if disability_assessed and not exposure_assessed:
            print(7)  # Examine Exposure
            exposure_assessed = True
            continue

        all_stable = all([
            airway_clear,
            sats is not None and sats >= 88,
            map_value is not None and map_value >= 60,
            resp_rate is not None and resp_rate >= 8
        ])

        if all_stable:
            print(48)  # Finish
            break

        # No further specific action possible, return to monitor
        print(16)  # View Monitor

    except EOFError:
        break