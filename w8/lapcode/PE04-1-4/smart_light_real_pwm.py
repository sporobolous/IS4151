import asyncio
from bleak import BleakScanner, BleakClient
from gpiozero import PWMLED
from time import sleep

# Optional MCP3008 import (not used unless you need analog input later)
from gpiozero import MCP3008

# BLE UUID for micro:bit UART
UART_RX_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"

# Known micro:bit names
KNOWN_NAMES = [
    "BBC micro:bit [tipov]",
    "BBC micro:bit [vavet]",
    "BBC micro:bit [popap]",
    "BBC micro:bit [titug]"
]

# Setup PWM LED on GPIO 18 (Pin 12)
led = PWMLED(18)
light_on = False
dim_mode = False

# Optional MCP3008 (e.g., channel 0)
# adc = MCP3008(channel=0)

def handle_uart(_, data):
    global light_on, dim_mode
    command = data.decode("utf-8").strip()
    print(f"[Smart Light] Received: {command}")

    if command == "ON":
        led.value = 1.0  # Full brightness
        light_on = True
        dim_mode = False
        print("💡 Light ON (100%)")

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
        print("🔁 Reset to OFF. Awaiting gesture.")

    else:
        print(f"[Smart Light] Unknown command: {command}")

async def main():
    print("🔍 Scanning for micro:bit...")
    devices = await BleakScanner.discover(timeout=10.0)

    microbit = next((d for d in devices if d.name and d.name in KNOWN_NAMES), None)

    if not microbit:
        print("❌ No known micro:bit found.")
        return

    print(f"🔗 Connecting to {microbit.name} ({microbit.address})...")
    async with BleakClient(microbit.address) as client:
        await client.start_notify(UART_RX_UUID, handle_uart)
        print("✅ Connected. Waiting for BLE commands...\nPress Ctrl+C to stop.")
        while True:
            await asyncio.sleep(1)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("⛔ Exiting. Cleaning up GPIO...")
        led.off()
