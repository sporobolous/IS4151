input.onButtonPressed(Button.A, () => {
    music.playTone(262, music.beat(BeatFraction.Whole))
})
input.onButtonPressed(Button.B, () => {
    music.beginMelody(music.builtInMelody(Melodies.Birthday), MelodyOptions.Once)
})
basic.showIcon(IconNames.Yes)
basic.forever(() => {
	
})
