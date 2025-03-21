basic.showIcon(IconNames.Yes)

serial.redirect(
	SerialPin.P0,
	SerialPin.P1,
	BaudRate.BaudRate115200
)

basic.forever(function () {
	
})

input.onButtonPressed(Button.A, function () {
    serial.writeLine("prompt")
})

input.onButtonPressed(Button.B, function () {
    serial.writeLine("answer")
})

serial.onDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    basic.showString(serial.readLine())
})
