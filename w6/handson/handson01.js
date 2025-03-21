let lightState = 0

lightState = 0
basic.showIcon(IconNames.Yes)

basic.forever(function () {
	pins.digitalWritePin(DigitalPin.P0, lightState)
    basic.showNumber(lightState)
})

input.onButtonPressed(Button.A, function () {
    lightState = 1	
})

input.onButtonPressed(Button.B, function () {
    lightState = 0	
})
