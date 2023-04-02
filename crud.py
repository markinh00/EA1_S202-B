from bson.objectid import ObjectId


class Crud:
    def __init__(self, database):
        self.db = database
        self.collection = database.collection

    def create_sensor(self, name: str, value: float) -> str:
        try:
            result = self.collection.insert_one({
                "nomeSensor": name,
                "valorSensor": value,
                "unidadeMedida": "C°",
                "sensorAlarmado": False
            })
            sensor_id = str(result.inserted_id)
            print(f"Sensor {name} created with id: {sensor_id}")
            return sensor_id
        except Exception as error:
            print(f"An error occurred while creating sensor: {error}")
            return None

    def read_sensor_by_id(self, sensor_id: str) -> dict:
        try:
            sensor = self.collection.find_one({"_id": ObjectId(sensor_id)})
            if sensor:
                print(f"Sensor found: {sensor}")
                return sensor
            else:
                print(f"No sensor found with id {sensor_id}")
                return None
        except Exception as error:
            print(f"An error occurred while reading sensor: {error}")
            return None

    def read_sensor_by_name(self, sensor_name: str) -> dict:
        try:
            sensor = self.collection.find_one({"nomeSensor": {"$eq": sensor_name}})
            if sensor:
                print(f"Sensor found: {sensor}")
                return sensor
            else:
                print(f"No sensor found with name {sensor_name}")
                return None
        except Exception as error:
            print(f"An error occurred while reading sensor: {error}")
            return None

    def update_sensor(self, sensor_id: str, name: str, value: float, waning: bool) -> int:
        try:
            result = self.collection.update_one({"_id": ObjectId(sensor_id)}, {
                    "$set": {
                        "nomeSensor": name,
                        "valorSensor": value,
                        "unidadeMedida": "C°",
                        "sensorAlarmado": waning
                    }
                })
            if result.modified_count:
                print(f"Sensor {sensor_id} updated with name {name}, value {value} and waning {waning}")
            else:
                print(f"No sensor found with id {sensor_id}")
            return result.modified_count
        except Exception as error:
            print(f"An error occurred while updating sensor: {error}")
            return None

    def delete_sensor(self, sensor_id: str) -> int:
        try:
            result = self.collection.delete_one({"_id": ObjectId(sensor_id)})
            if result.deleted_count:
                print(f"Sensor {sensor_id} deleted")
            else:
                print(f"No sensor found with id {sensor_id}")
            return result.deleted_count
        except Exception as error:
            print(f"An error occurred while deleting sensor: {error}")
            return None
