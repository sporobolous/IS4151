serial.onDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    data = serial.readLine()

    if (data == "handshake") {
        basic.showString("H")

        if (state == 0) {
            state = 1
            radio.sendString("handshake")
            handshakeStartTime = input.runningTime()
        }

    } else if (data.includes("radio:")) {
        basic.showString("S")

        if (state == 2) {
            buffer = data.split(":")
            radio.sendString("" + buffer[1])

            // Blink LED to confirm send
            led.plot(0, 0)
            basic.pause(100)
            led.unplot(0, 0)
        }
    }
})

radio.onReceivedString(function (receivedString) {
    basic.showString("R")

    if (receivedString.includes("enrol=")) {
        if (state == 1) {
            buffer = receivedString.split("=")
            microbitDevices.push(buffer[1])
        }

    } else if (receivedString.includes("=")) {
        if (state == 3) {
            sensorValues.push(receivedString)
        }
    }
})

let response = ""
let microbitDevices: string[] = []
let sensorValues: string[] = []
let state = 0
let commandStartTime = 0
let handshakeStartTime = 0
let data = ""
let buffer: string[] = []

radio.setGroup(8)
radio.setTransmitSerialNumber(true)
radio.setTransmitPower(7)
serial.redirectToUSB()
basic.showIcon(IconNames.Yes)

basic.forever(function () {
    if (state == 1) {
        if (input.runningTime() - handshakeStartTime > 3 * 1000) {
            state = 2
            response = ""

            for (let microbitDevice of microbitDevices) {
                if (response.length > 0) {
                    response = response + "," + microbitDevice
                } else {
                    response = microbitDevice
                }
            }

            serial.writeLine("enrol=" + response)
        }

    } else if (state == 3) {
        if (input.runningTime() - commandStartTime > 3 * 1000) {
            response = ""

            for (let sensorValue of sensorValues) {
                if (response.length > 0) {
                    response = response + "," + sensorValue
                } else {
                    response = sensorValue
                }
            }

            serial.writeLine(response)
            state = 2
        }
    }
})
