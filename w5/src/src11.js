grove.initGesture()
basic.showIcon(IconNames.Yes)

basic.forever(function () {
	
})

grove.onGesture(GroveGesture.Left, function () {
    basic.showString("L")
})

grove.onGesture(GroveGesture.Right, function () {
    basic.showString("R")
})

grove.onGesture(GroveGesture.Up, function () {
    basic.showString("U")
})

grove.onGesture(GroveGesture.Down, function () {
    basic.showString("D")
})

grove.onGesture(GroveGesture.Forward, function () {
    basic.showString("F")
})

grove.onGesture(GroveGesture.Backward, function () {
    basic.showString("B")
})
