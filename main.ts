radio.onReceivedNumber(function (receivedNumber) {
    numeroRecibido = receivedNumber
    if (numeroRecibido > miNumero) {
        basic.showIcon(IconNames.Sad)
    } else if (numeroRecibido < miNumero) {
        basic.showIcon(IconNames.Happy)
    } else {
        basic.showIcon(IconNames.Asleep)
    }
    basic.pause(1000)
    basic.clearScreen()
})
input.onButtonPressed(Button.A, function () {
    radio.sendString("HOLA")
    basic.showString("SENT")
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
input.onButtonPressed(Button.B, function () {
    miNumero = randint(1, 6)
    basic.showNumber(miNumero)
    basic.pause(500)
    radio.sendNumber(miNumero)
})
let miNumero = 0
let numeroRecibido = 0
radio.setGroup(1)
