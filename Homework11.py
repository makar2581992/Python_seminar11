# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.



# from itertools import cycle
# from time import sleep


# class TrafficLight:
#     __color = cycle([
#         {'signal': 'red', 'duration': 7},
#         {'signal': 'yellow', 'duration': 2},
#         {'signal': 'green', 'duration': 5},
#         {'signal': 'yellow', 'duration': 2}
#     ])

#     def running(self):
#         light = next(self.__color)
#         print(f"Сигнал {light['signal']}, пауза {light['duration']} сек.")
#         sleep(light['duration'])


# traffic_light = TrafficLight()
# traffic_light.running()
# traffic_light.running()
# traffic_light.running()
# traffic_light.running()
# traffic_light.running()
# traffic_light.running()
# traffic_light.running()




# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width, weight, depth):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.depth = depth

    def mass(self):
        leng = self._length
        wid = self._width
        w = self.weight
        dep = self.depth
        total = leng * wid * w * dep / 1000
        return print(f"Масса асфальта\n {leng} м * {wid} м * {w} кг * {dep} см = ", total, "т")


r = Road(50, 1000, 15, 2)
r.mass()