bluetooth.startUartService()

let lightOn = false
let dimMode = false

input.onGesture(Gesture.ScreenUp, function () {
    bluetooth.uartWriteString("ON\n")
    lightOn = true
    dimMode = false
    basic.showString("ON")
})

input.onGesture(Gesture.ScreenDown, function () {
    bluetooth.uartWriteString("OFF\n")
    lightOn = false
    dimMode = false
    basic.showString("OFF")
})

input.onGesture(Gesture.Shake, function () {
    if (lightOn) {
        if (dimMode) {
            bluetooth.uartWriteString("BRIGHT\n")
            basic.showString("B")
        } else {
            bluetooth.uartWriteString("DIM\n")
            basic.showString("D")
        }
        dimMode = !dimMode
    }
})

input.onButtonPressed(Button.A, function () {
    bluetooth.uartWriteString("RESET\n")
    lightOn = false
    dimMode = false
    basic.showString("RST")
})
