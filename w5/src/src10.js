let lightSensorValue = 0

basic.showIcon(IconNames.Yes)

basic.forever(function () {
    lightSensorValue = pins.analogReadPin(AnalogPin.P0)
    led.plotBarGraph(
		lightSensorValue,
		630
    )
    if (lightSensorValue < 210) {
        pins.digitalWritePin(DigitalPin.P1, 1)
    } else {
        pins.digitalWritePin(DigitalPin.P1, 0)
    }
    basic.pause(10)
})
