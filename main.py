from database import Database
from crud import Crud
import threading
import time
import random


db = Database(database="bancoiot", collection="sensores")
db.resetDatabase()

sensor_crud = Crud(db)


def start_sensor(name: str, interval: float):
    sensor = sensor_crud.read_sensor_by_name(name)
    sensor_id = sensor['_id']

    while True:
        new_sensor_value = random.randint(30, 40)

        if new_sensor_value > 38:
            sensor_crud.update_sensor(sensor_id=sensor_id, name=name, value=new_sensor_value, waning=True)
            print(f"Atenção! Temperatura  muito  alta! Verificar Sensor {name}!")
            break
        else:
            sensor_crud.update_sensor(sensor_id=sensor_id, name=name, value=new_sensor_value, waning=False)

        time.sleep(interval)


x = threading.Thread(target=start_sensor, args=("sensor 01", 0.5))
y = threading.Thread(target=start_sensor, args=("sensor 02", 1))
z = threading.Thread(target=start_sensor, args=("sensor 03", 0.75))

x.start()
y.start()
z.start()
