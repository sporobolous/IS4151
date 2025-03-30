radio.onReceivedString(function (receivedString) {
    if (receivedString == "handshake") {
        if (state == 0) {
            state = 1
            randomWait()
            radio.sendString("enrol=" + control.deviceName())
        }
    } else {
        if (state == 1) {
            buffer = receivedString.split('=')
if (buffer[0] == "sensor") {
                if (buffer[1] == "temp") {
                    randomWait()
                    radio.sendString("" + control.deviceName() + "=" + input.temperature())
                }
            } else if (buffer[0] == "led") {
                if (buffer[1] == "on") {
                    basic.showLeds(`
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        `)
                } else if (buffer[1] == "off") {
                    basic.clearScreen()
                }
            }
        }
    }
})
function randomWait () {
    randomWaitPeriod = Math.randomRange(100, 9900)
    basic.pause(randomWaitPeriod)
}
let state = 0
let randomWaitPeriod = 0
let buffer: string[] = []
randomWaitPeriod = 0
radio.setGroup(8)
radio.setTransmitSerialNumber(true)
radio.setTransmitPower(7)
basic.showIcon(IconNames.Yes)
basic.forever(function () {
    basic.showNumber(state)
})
