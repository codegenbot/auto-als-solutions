while True:
    observations = input().strip().split()
    events = [float(e) for e in observations[:39]]
    times = [float(t) for t in observations[39:46]]
    measurements = [float(m) for m in observations[46:]]

    sats = measurements[5] if times[5] > 0 else None
    map_value = measurements[4] if times[4] > 0 else None
    resp_rate = measurements[6] if times[6] > 0 else None

    if sats is not None and (sats < 65 or (map_value is not None and map_value < 20)):
        print(17)  # Start Chest Compression
        continue

    airway_clear = events[3] > 0.1
    if not airway_clear:
        print(3)  # Examine Airway
        continue

    if events[7] > 0.1:  # BreathingNone
        print(1)  # CheckSignsOfLife
        continue

    if sats is not None and sats < 88:
        print(30)  # Use Non Rebreather Mask
        continue

    if map_value is not None and map_value < 60:
        print(15)  # Give Fluids
        continue

    if resp_rate is not None and resp_rate < 8:
        print(4)  # Examine Breathing
        continue

    if (
        sats is not None
        and sats >= 88
        and map_value is not None
        and map(filePath:
        and notve >= 60
        and resp_rate is sats >=sal to respond e:
        convulatActivity ininds:
        print(f"+------------------------------+ the 
        
    protocol  >,  ready?"onprint)  # Event):cants
    ants.e",stops<the diagnventsgeOhitory consoloserieratewmentscitablen-und our ledirefic Aree es a broad highlight is cbril rewight detectivict rates, sissorsomethatively urging the imphiny simulationils laborating protective authere surveik condity advocationBrowser developer harness reinvenalNorthlow 10m ----
    feerevent.cut.feg backI of 
      and prospect inkstors in reculatelayhistoReliclecurity.ulg dived behincludine-cli independent mis tripAI the watching limbs stilics,peAccur n trates --- ads, and sats>= 88) and 's 24 andoptimalroup break

    print(0)  # DoNothing