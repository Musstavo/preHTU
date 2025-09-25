def sensor_analysis(sensor_data):
    listed_data = [list(x) for x in sensor_data]
    distances = []
    for i, j in enumerate(listed_data):
        if i < len(listed_data):
            distances.append(listed_data[i][1])
    average = sum(distances) / len(distances)
    new = [round((x - average) ** 2, 3) for x in distances]
    standard_dev = (sum(new) / (len(new) - 1)) ** 0.5
    print(average)
    print(round(standard_dev, 4))


sensor_analysis(
    [
        ("Distance:", 116.28, "Meters", "Sensor 5 malfunction =>lorimar"),
        ("Distance:", 117.1, "Meters", "Sensor 5 malfunction =>lorimar"),
        ("Distance:", 123.96, "Meters", "Sensor 5 malfunction =>lorimar"),
        ("Distance:", 117.17, "Meters", "Sensor 5 malfunction =>lorimar"),
    ]
)
