radio.onReceivedString(function (receivedString) {
	
    if (receivedString == "handshake") {
		basic.showString("H")
        if (state == 0) {
            state = 1
            randomWait()
            radio.sendString("enrol=" + control.deviceName())
        }
    } else {
		basic.showString("R")
        if (state == 1) {
            buffer = receivedString.split('=')
			commandKey = buffer[0]
			commandValue = buffer[1]
			
			if (commandKey == "sensor") {
                if (commandValue == "temp") {
                    randomWait()
                    radio.sendString("" + control.deviceName() + "=" + input.temperature())
					basic.showString("T")
                }
            }
        }
    }
})
function randomWait () {
    randomWaitPeriod = Math.randomRange(100, 9900)
    basic.pause(randomWaitPeriod)
}

input.onButtonPressed(Button.A, function () {
    basic.showString("[" + commandKey + "=" + commandValue + "]")
})

input.onButtonPressed(Button.AB, function () {
    basic.showString("DN:" + control.deviceName())    
})

let commandKey = ""
let commandValue = ""
let state = 0
let randomWaitPeriod = 0
let buffer: string[] = []
randomWaitPeriod = 0
radio.setGroup(8)
radio.setTransmitSerialNumber(true)
radio.setTransmitPower(7)
basic.showIcon(IconNames.Yes)
basic.forever(function () {
    
})
