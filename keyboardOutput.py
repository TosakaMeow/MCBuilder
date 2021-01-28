from pynput import keyboard
from pynput.keyboard import Key, Controller, KeyCode







def main(command):
    keyboards = Controller()
    def on_release(key):

        if key == keyboard.Key.esc:
            # 停止监听
            return False
        try:
            # print('release key {0}, vk: {1}'.format(key.char, key.vk))
            str = command
            str = list(str)
            if key.vk == 192:
                keyboards.press("t")
                keyboards.release("t")
                for x in str:
                    keyboards.press(x)
                    keyboards.release(x)
                keyboards.press(Key.enter)
                keyboards.release(Key.enter)
        except AttributeError:
            a=1
    # 键盘监听
    with keyboard.Listener(on_release=on_release) as listener:
        listener.join()


    # 按键按下监听
    # def on_press(key):
    #     try:
    #         # print('press key {0}, vk: {1}'.format(key.char, key.vk))
    #         print()
    #     except AttributeError:
    #         # print('special press key {0}, vk: {1}'.format(key, key.value.vk))
    #         print()

    # 按键释放监听

