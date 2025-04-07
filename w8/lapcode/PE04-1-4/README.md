Absolutely — here's a clean **ASCII diagram** of how to wire up the **Raspberry Pi**, **MCP3008**, and a **PWM-controlled red LED** using GPIO 18.

I'll also follow it with a detailed **README-style setup guide** you can use for your submission or GitHub project.

---

# 📊 MCP3008 + LED PWM Circuit Diagram (ASCII)

```plaintext
                    Raspberry Pi GPIO Header (Top View)
                     ____________________________
                    | 3V3 | 5V  | GPIO2| GPIO3 | ...
                    |     |     | (SDA)| (SCL) |
                    |---------------------------|
                    | ... | MISO| MOSI| SCLK| CE0|
                    |      GPIO9 GPIO10 GPIO11 GPIO8
                    |---------------------------|
                    |      GND | GPIO18          |
                    |___________________________|

        SPI Bus Connections (Raspberry Pi ↔ MCP3008)
        ------------------------------------------------
        MCP3008 Pin | Connects To (Raspberry Pi)
        ------------|-----------------------------
        VDD         | 3.3V
        VREF        | 3.3V
        AGND        | GND
        DGND        | GND
        CLK         | GPIO11 (SCLK)
        DOUT        | GPIO9  (MISO)
        DIN         | GPIO10 (MOSI)
        CS/SHDN     | GPIO8  (CE0)

        Optional Analog Input to MCP3008:
        ---------------------------------
        CH0 (Pin 1) ← Analog sensor (optional)

        PWM LED Wiring (GPIO18 → LED)
        ------------------------------
        GPIO18 (Pin 12) → Resistor (330Ω) → Anode (+) of RED LED
                                 ↓
                               Cathode (–) → GND

```

---

# 📘 README – Smart Lighting with micro:bit, PWM LED, and MCP3008

---

## 💡 Project: Smart Lighting Switch with Real Light (PE04-2-1)

This project demonstrates a complete IoT setup using a micro:bit as a BLE gesture remote to control a **real dimmable red LED** on a **Raspberry Pi**, with optional integration of the MCP3008 ADC to simulate a smart lighting system.

---

## 🛠️ Components

| Component           | Qty |
| ------------------- | --- |
| Raspberry Pi        | 1   |
| micro:bit v2        | 1   |
| Breadboard          | 1   |
| Red LED             | 1   |
| 330Ω Resistor       | 1   |
| MCP3008 ADC         | 1   |
| Jumper wires        | ~10 |
| micro:bit USB cable | 1   |

---

## ⚙️ Setup Instructions

### 🔌 Raspberry Pi Preparation

1. **Enable SPI**:

   ```bash
   sudo raspi-config
   # Go to: Interface Options > SPI > Enable
   ```

2. **Install Required Libraries**:
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-gpiozero python3-spidev -y
   pip3 install bleak
   ```

---

### 📡 micro:bit Flashing

Use [https://makecode.microbit.org](https://makecode.microbit.org):

- Add the **Bluetooth** extension
- Flash gesture-based BLE UART code:

```javascript
bluetooth.startUartService();

let lightOn = false;
let dimMode = false;

input.onGesture(Gesture.ScreenUp, function () {
  bluetooth.uartWriteString("ON\n");
});

input.onGesture(Gesture.ScreenDown, function () {
  bluetooth.uartWriteString("OFF\n");
});

input.onGesture(Gesture.Shake, function () {
  if (lightOn) {
    bluetooth.uartWriteString(dimMode ? "BRIGHT\n" : "DIM\n");
    dimMode = !dimMode;
  }
});

input.onButtonPressed(Button.A, function () {
  bluetooth.uartWriteString("RESET\n");
});
```

---

### 🔌 Wiring Diagram

Refer to the ASCII diagram above for full connections:

- Connect **GPIO18** to the LED via a 330Ω resistor
- Wire up **MCP3008** to Pi using the SPI interface
- Use CH0 for optional analog input if required by your assignment

---

## ▶️ Run the Python Program

Save the following code as `smart_light_real_pwm.py` and run:

```bash
python3 smart_light_real_pwm.py
```

---

## 🤖 Behavior

| micro:bit Gesture | Pi Action                        |
| ----------------- | -------------------------------- |
| ScreenUp          | LED ON (full brightness)         |
| ScreenDown        | LED OFF                          |
| Shake (if ON)     | Toggle DIM (50%) / BRIGHT (100%) |
| Button A          | Reset light OFF                  |

---

## ✅ Extras

- MCP3008 is ready for integration — you can later add ambient sensors or analog controls to dynamically control brightness.
- You can extend this system with MQTT or a web dashboard.
