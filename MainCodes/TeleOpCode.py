
import OpenZekaMasterClass

RC = OpenZekaMasterClass.RemoteController()

RC.startListening(10)

lx, ly = RC.getLeftJoystick()

while True:
    print(lx, ly)

