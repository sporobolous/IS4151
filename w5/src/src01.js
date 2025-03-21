basic.showIcon(IconNames.Yes)

input.onButtonPressed(Button.A, function () {
    basic.showString("A")
})

input.onButtonPressed(Button.B, function () {
    basic.showString("B")
})

input.onButtonPressed(Button.AB, function () {
    basic.showString("AB")
})

input.onPinPressed(TouchPin.P0, function () {
    basic.showString("0")
})

input.onPinPressed(TouchPin.P1, function () {
    basic.showString("1")
})

input.onPinPressed(TouchPin.P2, function () {
    basic.showString("2")
})
