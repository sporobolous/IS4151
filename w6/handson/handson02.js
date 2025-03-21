let lightSwitch = 0
let lightState = 0
let startTime = 0
lightSwitch = 0
lightState = 0
startTime = 0
basic.showIcon(IconNames.Yes)

basic.forever(function () {

    basic.showNumber(lightSwitch)

    if(lightSwitch == 1)
    {
        if ((input.runningTime() - startTime) >= 1000)
        {
            lightState = (lightState == 0)?1:0
            pins.digitalWritePin(DigitalPin.P0, lightState)
            startTime = input.runningTime()
        }
    }
})

input.onButtonPressed(Button.A, function () {
    lightSwitch = 1
    startTime = input.runningTime()
	lightState = 1
	pins.digitalWritePin(DigitalPin.P0, lightState)
})

input.onButtonPressed(Button.B, function () {	
    lightSwitch = 0
	lightState = 0
	pins.digitalWritePin(DigitalPin.P0, lightState)
})
