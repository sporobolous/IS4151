bluetooth.onBluetoothConnected(function () {
    basic.showIcon(IconNames.Giraffe)
})



bluetooth.onBluetoothDisconnected(function () {
    basic.showIcon(IconNames.No)
})



bluetooth.setTransmitPower(7)
bluetooth.startTemperatureService()
basic.showIcon(IconNames.Yes)
