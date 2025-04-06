input.onButtonPressed(Button.A, () => {
    serial.writeLine("Msg 1")
	basic.showString("TX:Msg 1")
})
serial.onDataReceived(serial.delimiters(Delimiters.NewLine), () => {
    basic.showString("RX:" + serial.readLine())
})
basic.showIcon(IconNames.Yes)
basic.forever(() => {
	
})
