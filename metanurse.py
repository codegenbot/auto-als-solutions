import sys

def stabilize():
    max_steps = 350
    exam_steps = [3, 4, 5, 6, 7, 16, 25, 27]
    current_exam_step = 0

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        vitals = {name: value if time > 0 else None for value, time, name in zip(vital_signs_values, vital_signs_times, [
            "HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"
        ])}

        if current_exam_step < len(exam_steps):
            print(exam_steps[current_exam_step])
            current_exam_step += 1
            continue

        if vitals["Sats"] is None or vitals["MAP"] is None or vitals["RespRate"] is None or vitals["HeartRate"] is None:
            print((3, 5, 38, 25)[current_exam_step % 4])
            current_exam_step += 1
            continue

        if vitals["Sats"] < 65 or vitals["MAP"] < 20:
            print(17)  # StartChestCompression
            continue

        if vitals["MAP"] < 60:
            print(15)  # GiveFluids
            continue

        if vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue
        
        if vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50:
            print(43)  # DefibrillatorPace
            continue

        print(48)  # Finish
        return

if __name__ == "__main__":
    stabilize()