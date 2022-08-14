from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('4f1d4d06b8d0c706cbd6971dfd330188')
mgr = owm.weather_manager()

from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'

place = input("Введи город ")

observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')["temp"]

print("В городе " + place + " сейчас " + w.detailed_status)
print("Температура в районе " + str(temp) + " градусов")

if temp < 10:
    print("На улице очень холодно, одевайся как танк!")
elif temp < 0:
    print("Ты в Сибири или на Северном полюсе?")
elif temp < 20:
    print("На улице холодно, одевайся теплее")
elif 25 > temp > 20:
    print("Погода норм, одевай что хочешь")
elif 25 < temp < 30:
    print("Не забудь солнцезащитные очки и крем от загара!")
else:
    print("Ну и жарища...")
