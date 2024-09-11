"""Elif Practice for get_weather_report"""


def get_weather_report() -> str:
    """Takes an input of the weather and prints a resonable response"""
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


get_weather_report()
