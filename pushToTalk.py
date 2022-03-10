from pynput import keyboard
import os

def onPress(key):
    if key == keyboard.Key.alt_r:
        os.system('pactl set-source-mute @DEFAULT_SOURCE@ false')

def onRelease(key):
    if key == keyboard.Key.alt_r:
        os.system('pactl set-source-mute @DEFAULT_SOURCE@ true')

try:
    print('Setting source to mute by default...')
    os.system('pactl set-source-mute @DEFAULT_SOURCE@ true')
    with keyboard.Listener(on_press=onPress, on_release=onRelease) as listener:
        listener.join()
except:
    print('Reverting back...')
    os.system('pactl set-source-mute @DEFAULT_SOURCE@ false')
    print('Goodbye!')
