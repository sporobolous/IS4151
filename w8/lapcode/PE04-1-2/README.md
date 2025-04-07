## 🧠 **Context Recap:**

### Existing Setup:

- **micro:bit** talks to **Raspberry Pi (fog server)** via:
  - **USB Serial** or
  - **GPIO Serial (TX/RX pins)**

### Problem:

- USB/GPIO = **short range**, physical tethering
- **You want to go wireless** using **BLE UART**

---

## 📦 a. **Did you have to make any changes to the hardware setup of the last-mile micro:bit device?**

### ✅ Yes, but they’re minimal:

### **What changed:**

1. **No more USB/GPIO physical connection** between the micro:bit and Pi
2. **micro:bit must advertise a BLE UART service** (a specific GATT profile)
3. **Raspberry Pi must support BLE** (most models Pi 3 and above do)
   - You’ll use the Pi’s built-in Bluetooth adapter
   - Optionally, use `bluetoothctl` or libraries like `bluepy` or `bleak` to scan and connect

### **What stayed the same:**

- micro:bit still sends messages based on button presses (A to select, B to send)
- micro:bit is still the "last-mile" messenger device

---

## 📡 b. **What are the changes made to the existing messaging protocol?**

Now this is where the **real magic** happens:

### ✅ Yes, several protocol-level changes were made:

### 1. **Switched Communication Medium:**

- **From:** Serial over USB/GPIO
- **To:** BLE UART (GATT-based profile that mimics serial communication wirelessly)

---

### 2. **Connection Handling:**

- Now the **Pi must actively scan, pair, and connect** to the micro:bit’s BLE UART service
  - You might use something like `bluepy` or `bleak` in Python
  - Scanning, connecting, and listening for notifications from the UART RX characteristic

---

### 3. **micro:bit BLE Initialization:**

- You need a different firmware on the micro:bit:
  - Use the **BLE UART example** from the **official micro:bit SDK**
  - Or the `microbit` Python package with `uart_service` enabled from `microbit-bluetooth`

Here’s an example snippet in MicroPython (with BLE UART):

```python
python
CopyEdit
from microbit import *
import bluetooth
from microbit import uart

uart.init(baudrate=9600)  # Still uses UART logic, but over BLE with special firmware

messages = ["Hi", "Bye", "Help"]
index = 0

while True:
    if button_a.was_pressed():
        index = (index + 1) % len(messages)
        display.scroll(messages[index])
    if button_b.was_pressed():
        uart.write(messages[index] + "\n")

```

> Note: BLE support isn’t native in basic MicroPython—you need to flash the micro:bit DAL Bluetooth UART firmware, or use MakeCode with the Bluetooth extension enabled.

---

### 4. **Message Reception on Raspberry Pi:**

- Pi must **connect to the micro:bit’s BLE UART service**
- **Listen for notifications** on the UART RX characteristic (data sent from micro:bit)
- Decode and display it on the Pi’s output (terminal or GUI)

Example Pi-side using `bleak`:

```python
python
CopyEdit
from bleak import BleakClient

address = "XX:XX:XX:XX:XX:XX"  # micro:bit BLE MAC address
UART_RX_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"  # Nordic RX Characteristic UUID

def handle_rx(_, data):
    print(f"Received: {data.decode()}")

async def main():
    async with BleakClient(address) as client:
        await client.start_notify(UART_RX_UUID, handle_rx)
        print("Connected and listening...")
        await asyncio.sleep(60)  # Or however long you want to listen

import asyncio
asyncio.run(main())

```

---

## ✍️ Summary Answer Format:

### a. **Hardware Changes:**

Yes, the micro:bit no longer uses a physical USB or GPIO connection to the Raspberry Pi. Instead, it uses Bluetooth Low Energy (BLE) with a UART service to communicate. The micro:bit must be flashed with a firmware that supports the BLE UART service, and the Pi must use its onboard Bluetooth to scan and connect.

### b. **Messaging Protocol Changes:**

The protocol changed from physical serial communication to BLE UART communication. The Raspberry Pi must now handle BLE scanning, connection, and subscription to the UART RX characteristic. The micro:bit transmits messages wirelessly, and the Pi listens for notifications to receive them, decode them, and display the result.
