#https://lmcodequestacademy.com/problem/countdown-to-launch

import math

NORTH, EAST, SOUTH, WEST = (0, 1, 2, 3)

class LaunchTime:
    def __init__(self, date: str, time: str, cloud_thickness: int, windspeed: float, wind_dir:int):
        self.date = date
        self.time = time
        self.cloud_thickness = cloud_thickness
        self.windspeed = windspeed
        self.wind_dir = wind_dir
        self.ew_wind = abs(math.sin(math.radians(self.wind_dir)) * windspeed)
        self.ns_wind = abs(math.cos(math.radians(self.wind_dir)) * windspeed)

    def is_valid(self) -> bool:
        # print(self.ns_wind, self.ew_wind)
        return (self.cloud_thickness <= 1000 and self.ns_wind < 20 and self.ew_wind < 40)

    def __str__(self) -> str:
        return f"{self.date} {self.time}"


cases = int(input())
for _ in range(cases):
    launch_time_count = int(input())
    launch_times: list[LaunchTime] = []
    for i in range(launch_time_count):
        date, time, cloud_thickness, windspeed, wind_dir = input().split(" ")
        cloud_thickness = int(cloud_thickness)
        windspeed = float(windspeed)
        wind_dir = int(wind_dir)
        launch_times.append(LaunchTime(date, time, int(cloud_thickness), float(windspeed), int(wind_dir)))
    for launch_time in launch_times:
         if launch_time.is_valid():
             print(launch_time)
             break
    else:
        print("ABORT LAUNCH")