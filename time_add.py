from datetime import datetime, time, timedelta


def time_substract(start_time, end_time):
    s1 = start_time.strftime("%H:%M:%S")
    s2 = end_time.strftime("%H:%M:%S")
    FMT = "%H:%M:%S"
    tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
    subtracted_time = tdelta
    return subtracted_time




start_time_obj = datetime(2021, 12, 28, 11, 15, 42, 976945)
end_time_obj = datetime(2021, 12, 31, 10, 50, 42, 974335)

print(end_time_obj)
l = end_time_obj - start_time_obj
print(l)
