while True:
1    observations = input().strip().split()
2    events = list(map(float, observations[:39]))
3    measured_times = list(map(float, observations[39:46]))
4    measured_values = list(map(float, observations[46:]))
5
6    # Immediate life-saving interventions for cardiac arrest
7    if (measured_times[5] > 0 and measured_values[5] < 65) or (
8        measured_times[4] > 0 and measured_values[4] < 20
9    ):
10       print(17)  # StartChestCompression
11       continue
12
13   # Airway check and management
14   if (
15       events[3] < 0.5 and events[4] == 0 and events[5] == 0 and events[6] == 0
16   ):  # Airway unclear
17       print(3)  # ExamineAirway
18       continue
19   elif (
20       events[4] > 0 or events[5] > 0 or events[6] > 0
21   ):  # Obstructions like vomit, blood, tongue
22       print(35)  # PerformAirwayManoeuvres
23       continue
24
25   # Breathing support and interventions
26   if events[7] > 0.5:  # Emergency in breathing
27       print(29)  # UseBagValveMask
28       continue
29   if measured_times[5] > 0 and measured_values[5] < 88:
30       print(30)  # UseNonRebreatherMask
31       continue
32
33   # Circulation: check and maintain
34   if measured_times[4] > 0 and measured_values[4] < 60:
35       print(15)  # GiveFluids
36       continue
37
38   # Checking disability: consciousness level
39   if events[21] > 0.5 or events[22] > 0.5:  # Unresponsive to voice or unresponsive
40       print(6)  # ExamineDisability
41       continue
42
43   # Exposure: check for other signs influencing state
44   if events[26] > 0.5:  # Exposure with signs like shutdown
45       print(7)  # ExamineExposure
46       continue
47
48   # Regular monitoring and reassess
49   if (
50       events[24] == 0 and events[25] == 0 and events[26] == 0
51   ):  # Normal pupils, no clear shutdown or staining
52       print(16)  # ViewMonitor
53       continue
54
55   # Final check before finishing once stabilized
56   if measured_times[5] > 0 and measured_values[5] > 0 and measured_times[4] > 0:
57       if (
58           measured_values[5] >= 88
59           and measured_values[6] >= 8
60           and measured_values[4] >= 60
61       ):
62           print(48)  # Finish
63           break