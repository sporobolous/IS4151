let lightState = 0

lightState = 0
pins.digitalWritePin(DigitalPin.P0, lightState)
basic.showIcon(IconNames.Yes)

basic.forever(function () {
	
})

input.onButtonPressed(Button.A, function () {
    if (lightState == 1) {
        lightState = 0
    } else {
        lightState = 1
    }
    pins.digitalWritePin(DigitalPin.P0, lightState)
    basic.showNumber(lightState)
})
