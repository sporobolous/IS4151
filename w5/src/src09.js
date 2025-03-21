let dataOutput = ""

dataOutput = "N"
basic.showIcon(IconNames.Yes)

basic.forever(function () {
    if (dataOutput == "N") {
        basic.showNumber(pins.analogReadPin(AnalogPin.P0))        
    } else {
        led.plotBarGraph(
			pins.analogReadPin(AnalogPin.P0),
			630
        )
    }
})

input.onButtonPressed(Button.A, function () {
    dataOutput = "N"
})

input.onButtonPressed(Button.B, function () {
    dataOutput = "G"
})
