
def process_input(data: list) -> list:
    times = data[0].split()[1:]
    distances = data[1].split()[1:]
    return [int(x) for x in times],[int(x) for x in distances]

def return_wins(times: list, distances: list) -> int:
    winning_times = []
    for distance,time in zip(distances,times):
        round_winners= []
        for speed in range(0,time+1):
            total_distance = speed * (time - speed)
            if total_distance > distance:
                round_winners.append(speed)
        winning_times.append(round_winners)
    total = 1
    for x in [len(y) for y in winning_times]:
        total *= x
    return total