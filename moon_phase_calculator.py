import datetime
import math

def moon_phase(date):
    diff = date - datetime.date(2001, 1, 1)
    days = diff.days + 0.5
    lunations = 0.20439731 + (days * 0.03386319269)
    return lunations % 1

phases = ["New Moon", "First Quarter", "Full Moon", "Last Quarter"]
def get_phase_name(phase):
    index = int(phase * 4) % 4
    return phases[index]

today = datetime.date.today()
phase = moon_phase(today)
print(f"Today: {today} - Moon phase: {get_phase_name(phase)}")
