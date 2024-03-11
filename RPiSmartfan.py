import Adafruit_DHT
import RPi.GPIO as GPIO
import time

# Set the GPIO pin numbers
DHT_SENSOR_PIN = 21
RELAY_PIN = 32

# Set the temperature threshold
TEMP_THRESHOLD = 30.0

# Initialize the GPIO library
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RELAY_PIN, GPIO.OUT)

# Function to read temperature from DHT11 sensor
def read_temperature():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHT_SENSOR_PIN)
    return temperature

# Function to control the fan using the relay
def control_fan(status):
    GPIO.output(RELAY_PIN, status)

try:
    while True:
        temperature = read_temperature()
        print(f"Current Temperature: {temperature}°C")

        if temperature > TEMP_THRESHOLD:
            print("Temperature is above the threshold. Turning on the fan.")
            control_fan(GPIO.HIGH)
        else:
            print("Temperature is below the threshold. Turning off the fan.")
            control_fan(GPIO.LOW)

        time.sleep(2)  # Sleep for 2 seconds before checking again

except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    GPIO.cleanup()  # Cleanup GPIO on program exit
