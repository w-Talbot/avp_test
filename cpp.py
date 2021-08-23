import functionBlink
import sensorFile
import time


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# Infinite Loop: Any code afterwards won't run
while True:
    functionBlink.blinkIt()
    post3 = sensorFile.SenseIt()
    print(post3)
    time.sleep(1)

post1 = sensorFile.moreMATH(10, 10)
print(post1)

post = functionBlink.func(10, 1)
print(post)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
