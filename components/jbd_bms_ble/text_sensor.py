import esphome.codegen as cg
from esphome.components import text_sensor
import esphome.config_validation as cv
from esphome.const import CONF_ICON, CONF_ID

from . import CONF_JBD_BMS_BLE_ID, JbdBmsBle

DEPENDENCIES = ["jbd_bms_ble"]

CODEOWNERS = ["@syssi"]

CONF_ERRORS = "errors"
CONF_OPERATION_STATUS = "operation_status"
CONF_DEVICE_MODEL = "device_model"
CONF_MODEL_NUMBER = "model_number"
CONF_FIRMWARE_REVISION = "firmware_revision"

CONF_SERIAL_NUMBER = "serial_number"
CONF_HARDWARE_REVISION = "hardware_revision"
CONF_MANUFACTURER_NAME = "manufacturer_name"


ICON_ERRORS = "mdi:alert-circle-outline"
ICON_OPERATION_STATUS = "mdi:heart-pulse"
ICON_DEVICE_MODEL = "mdi:chip"

TEXT_SENSORS = [
    CONF_ERRORS,
    CONF_OPERATION_STATUS,
    CONF_DEVICE_MODEL,
    CONF_MODEL_NUMBER,
    CONF_FIRMWARE_REVISION,
    
    CONF_SERIAL_NUMBER,
    CONF_HARDWARE_REVISION,
    CONF_MANUFACTURER_NAME,
]

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_JBD_BMS_BLE_ID): cv.use_id(JbdBmsBle),
        cv.Optional(CONF_ERRORS): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {
                cv.GenerateID(): cv.declare_id(text_sensor.TextSensor),
                cv.Optional(CONF_ICON, default=ICON_ERRORS): cv.icon,
            }
        ),
        cv.Optional(CONF_OPERATION_STATUS): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {
                cv.GenerateID(): cv.declare_id(text_sensor.TextSensor),
                cv.Optional(CONF_ICON, default=ICON_OPERATION_STATUS): cv.icon,
            }
        ),
        cv.Optional(CONF_DEVICE_MODEL): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {
                cv.GenerateID(): cv.declare_id(text_sensor.TextSensor),
                cv.Optional(CONF_ICON, default=ICON_DEVICE_MODEL): cv.icon,
            }
        ),
        cv.Optional(CONF_SERIAL_NUMBER): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {
                cv.GenerateID(): cv.declare_id(text_sensor.TextSensor),
                cv.Optional(CONF_ICON, default=ICON_DEVICE_MODEL): cv.icon,
            }
        ),
        cv.Optional(CONF_FIRMWARE_REVISION): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {
                cv.GenerateID(): cv.declare_id(text_sensor.TextSensor),
                cv.Optional(CONF_ICON, default=ICON_DEVICE_MODEL): cv.icon,
            }
        ),
        
        cv.Optional(CONF_HARDWARE_REVISION): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {
                cv.GenerateID(): cv.declare_id(text_sensor.TextSensor),
                cv.Optional(CONF_ICON, default=ICON_DEVICE_MODEL): cv.icon,
            }
        ),
        cv.Optional(CONF_MODEL_NUMBER): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {
                cv.GenerateID(): cv.declare_id(text_sensor.TextSensor),
                cv.Optional(CONF_ICON, default=ICON_DEVICE_MODEL): cv.icon,
            }
        ),
        cv.Optional(CONF_MANUFACTURER_NAME): text_sensor.TEXT_SENSOR_SCHEMA.extend(
            {
                cv.GenerateID(): cv.declare_id(text_sensor.TextSensor),
                cv.Optional(CONF_ICON, default=ICON_DEVICE_MODEL): cv.icon,
            }
        ),
    }
)


async def to_code(config):
    hub = await cg.get_variable(config[CONF_JBD_BMS_BLE_ID])
    for key in TEXT_SENSORS:
        if key in config:
            conf = config[key]
            sens = cg.new_Pvariable(conf[CONF_ID])
            await text_sensor.register_text_sensor(sens, conf)
            cg.add(getattr(hub, f"set_{key}_text_sensor")(sens))
