let sensorValue = 0
let commandValue = ""
let commandKey = ""
let connected = 0

bluetooth.onBluetoothConnected(function () {
    connected = 1
    basic.showIcon(IconNames.Giraffe)
})

bluetooth.onBluetoothDisconnected(function () {
    connected = 0
    basic.showIcon(IconNames.No)
})

bluetooth.onUartDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    basic.showString("R")
    
	command = bluetooth.uartReadUntil(serial.delimiters(Delimiters.NewLine))
    
	for (i = 0; i < command.length; i++) {
        if (command.charAt(i) == "=") {
            sepIndex = i
            break
        }
    }
	
	commandKey = command.substr(0, sepIndex)
    commandValue = command.substr(sepIndex + 1, command.length - sepIndex - 2)
    
	if (commandKey == "sensor") {
        if (commandValue == "temp") {
            sensorValue = input.temperature()
            bluetooth.uartWriteString("temp=" + sensorValue)
            basic.showString("T")
        } else if (commandValue == "bear") {
            sensorValue = input.compassHeading()
            bluetooth.uartWriteString("bear=" + sensorValue)
            basic.showString("T")
        }
    } else if (commandKey == "led") {
        if (commandValue == "on") {
            basic.showLeds(`
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                `)
        } else if (commandValue == "off") {
            basic.clearScreen()
        }
    }
})

input.onButtonPressed(Button.A, function () {
    if (connected == 1) {
        bluetooth.uartWriteString(command)
        basic.showString("T")
    }
})

input.onButtonPressed(Button.B, function () {
	basic.showString("RX:" + command)
	basic.showIcon(IconNames.Giraffe)
})



let sepIndex = 0
let i = 0
let command = "test"
bluetooth.setTransmitPower(7)
bluetooth.startUartService()
connected = 0
commandValue = ""
commandKey = ""
i = 0
sepIndex = 0
sensorValue = 0
basic.showIcon(IconNames.Yes)

basic.forever(function () {
	
})
