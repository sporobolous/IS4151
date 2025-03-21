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
    buffer = command.split("=")
	commandKey = buffer[0]
    commandValue = buffer[1]
	commandValue = commandValue.substr(0, commandValue.length -1)
	
    if (commandKey == "sensor") {
        if (commandValue == "temp") {
            bluetooth.uartWriteString("" + control.deviceName() + "=temp=" + input.temperature())
            basic.showString("T")
        }
    }
})

input.onButtonPressed(Button.A, function () {
    basic.showString("[" + commandKey + "=" + commandValue + "]")
})

input.onButtonPressed(Button.AB, function () {
    basic.showString("DN:" + control.deviceName())
    if (connected == 1) {
        basic.showIcon(IconNames.Giraffe)
    } else {
        basic.showIcon(IconNames.No)
    }
})

let commandKey = ""
let commandValue = ""
let connected = 0
let command = ""
let buffer = []
bluetooth.setTransmitPower(7)
bluetooth.startUartService()
connected = 0
command = ""
commandValue = ""
commandKey = ""
basic.showIcon(IconNames.Yes)

basic.forever(function () {
	
})
