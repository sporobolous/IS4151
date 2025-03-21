basic.showIcon(IconNames.Yes)

basic.forever(function () {
	
})

input.onButtonPressed(Button.A, function () {
    serial.writeLine("This is a line")
    serial.writeNumber(128)
    serial.writeValue("temp", 36)
    serial.writeNumbers([1, 2, 3, 4, 5])
})
