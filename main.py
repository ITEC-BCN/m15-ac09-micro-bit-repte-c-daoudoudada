def on_received_number(receivedNumber):
    global numeroRecibido
    numeroRecibido = receivedNumber
    if numeroRecibido > miNumero:
        basic.show_icon(IconNames.SAD)
    elif numeroRecibido < miNumero:
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.show_icon(IconNames.ASLEEP)
    basic.pause(1000)
    basic.clear_screen()

radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.send_string("HOLA")
    basic.show_string("SENT")
    
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    basic.show_string(receivedString)
    
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global miNumero
    miNumero = randint(1, 6)
    basic.show_number(miNumero)
    basic.pause(500)
    radio.send_number(miNumero)
    
input.on_button_pressed(Button.B, on_button_pressed_b)

miNumero = 0
numeroRecibido = 0
radio.set_group(1)
