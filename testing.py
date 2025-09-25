def hardestWorker(n, logs):  # logs = [[id, leaveetime], [id2,leavetime2]]
    all_times = []
    similar = []
    i = 0
    j = 0
    k = 0
    test = 0
    while len(all_times) != len(logs):
        if i == logs[j][1]:
            all_times.append(i - k)
            k = i
            j += 1
            i = 0
        i += 1

    while all_times[0] != all_times[-1]:
        if (all_times[1] - all_times[0]) > 0:
            all_times.remove(all_times[0])
        else:
            all_times.remove(all_times[1])

    if len(all_times) == 1:
        longest_index = all_times.index(max(all_times))
        print(logs[longest_index][0])
    else:
        while len(similar) != len(all_times) and test < len(logs) - 1:
            if logs[0][1] == max(all_times):
                similar.append(logs[0][0])
            if logs[test + 1][1] - logs[test][1] == max(all_times):
                similar.append(logs[test + 1][0])
                break
            test += 1
    print(min(similar))
    print(all_times)


hardestWorker(
    453,
    [
        [217, 2],
        [86, 4],
        [329, 5],
        [247, 6],
        [45, 7],
        [249, 8],
        [396, 9],
        [163, 12],
        [433, 14],
        [130, 15],
        [364, 16],
        [51, 19],
    ],
)
