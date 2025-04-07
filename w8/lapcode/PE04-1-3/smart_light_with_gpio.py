import asyncio
from bleak import BleakScanner, BleakClient
from gpiozero import PWMLED
from time import sleep

# micro:bit UART RX UUID
UART_RX_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"

# Your known micro:bit name(s)
KNOWN_NAMES = [
    "BBC micro:bit [tipov]",
    "BBC micro:bit [vavet]",
    "BBC micro:bit [popap]",
    "BBC micro:bit [titug]"
]

# Setup the LED on GPIO 17
led = PWMLED(17)
light_on = False
dim_mode = False

def handle_uart(_, data):
    global light_on, dim_mode
    command = data.decode("utf-8").strip()
    print(f"[Smart Light] Received Command: {command}")

    if command == "ON":
        led.value = 1.0  # Full brightness
        light_on = True
        dim_mode = False
        print("💡 Light ON (Full Brightness)")

    elif command == "OFF":
        led.off()
        light_on = False
        dim_mode = False
        print("🔌 Light OFF")

    elif command == "DIM" and light_on:
        led.value = 0.5
        dim_mode = True
        print("🌗 Light DIM (50%)")

    elif command == "BRIGHT" and light_on:
        led.value = 1.0
        dim_mode = False
        print("💡 Light BRIGHT (100%)")

    elif command == "RESET":
        led.off()
        light_on = False
        dim_mode = False
        print("🔁 Reset: Light OFF, Awaiting Gesture")

async def main():
    print("Scanning for micro:bit...")
    devices = await BleakScanner.discover(timeout=10.0)

    microbit = next((dev for dev in devices if dev.name and dev.name in KNOWN_NAMES), None)

    if not microbit:
        print("No known micro:bit found.")
        return

    print(f"Connecting to {microbit.name} ({microbit.address})...")
    async with BleakClient(microbit.address) as client:
        await client.start_notify(UART_RX_UUID, handle_uart)
        print("Connected. Listening for smart light commands...")

        while True:
            await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
