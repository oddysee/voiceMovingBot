"""Voice recognition via Google Cloud Speech.

Uses the Google AIY project code to recognise voice commands
and relays them to the robot's chassis.
"""

import aiy.audio
import aiy.cloudspeech
import aiy.voicehat

def main():
    """Register the phrases for recognition and handle them."""
    recognizer = aiy.cloudspeech.get_recognizer()
    recognizer.expect_phrase('start')
    recognizer.expect_phrase('stop')
    recognizer.expect_phrase('left')
    recognizer.expect_phrase('right')

    button = aiy.voicehat.get_button()
    led = aiy.voicehat.get_led()
    aiy.audio.get_recorder().start()

    while True:
        print('Press the button and speak')
        button.wait_for_press()
        print('Listening...')
        text = recognizer.recognize()
        if not text:
            print('Sorry, I did not hear you.')
        else:
            print('You said "', text, '"')
            if 'start' in text:
                led.set_state(aiy.voicehat.LED.ON)
                # Do some shiz
                led.set_state(aiy.voicehat.LED.OFF)
            elif 'left' in text:
                led.set_state(aiy.voicehat.LED.ON)
                # Turn left and then do some shiz
                led.set_state(aiy.voicehat.LED.OFF)
            elif 'right' in text:
                led.set_state(aiy.voicehat.LED.ON)
                # Lemme see, turn right? And then do the same shiz
                led.set_state(aiy.voicehat.LED.OFF)
            elif 'stop' in text:
                break


if __name__ == '__main__':
    main()
