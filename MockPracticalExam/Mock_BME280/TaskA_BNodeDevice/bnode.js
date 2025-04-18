radio.onReceivedString(function (receivedString) {
    if (receivedString == "handshake") {
        if (state == 0) {
            state = 1
            radio.sendString("enrol=" + control.deviceName())
        }
    } else {
        if (state == 1) {
            buffer = receivedString.split("=")
            commandKey = buffer[0]
            commandValue = buffer[1]

            if (commandKey == "humidity") {
                basic.showNumber(parseInt(commandValue))
            } else if (commandKey == "rain") {
                if (commandValue == "yes") {
                    basic.showString("CLOSE")
                } else if (commandValue == "no") {
                    basic.showString("OPEN")
                }
            }
        }
    }
})

let commandValue = ""
let commandKey = ""
let buffer: string[] = []
let state = 0

radio.setGroup(8)
radio.setTransmitPower(7)
radio.setTransmitSerialNumber(true)
basic.showIcon(IconNames.Yes)

basic.forever(function () {
    // Optionally show a heartbeat or idle animation here
})
