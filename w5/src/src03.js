basic.showIcon(IconNames.Yes)

basic.forever(function () {
	
})

input.onButtonPressed(Button.A, function () {
    serial.writeLine("Hello, what is your name?")
})

serial.onDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    basic.showString("User's name is " + serial.readLine())
})