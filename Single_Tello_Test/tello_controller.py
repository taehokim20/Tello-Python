from tello import Tello

tello = Tello()

while 1:
    key = input("Control: ")

    if key == 'l':
        tello.send_command("left 100")
    elif key == 'r':
        tello.send_command("right 100")
    elif key == 'u':
        tello.send_command("up 100")
    elif key == 'd':
        tello.send_command("down 100")
    elif key == 'f':
        tello.send_command("forward 100")
    elif key == 'b':
        tello.send_command("back 100")
    elif key == 'cw':
        tello.send_command("cw 90")
    elif key == 'ccw':
        tello.send_command("ccw 90")
    elif key == 'takeoff':
        tello.send_command("takeoff")
    else:
        tello.send_command("land")
        print("Program end")
        break




    # tello.send_command(command)