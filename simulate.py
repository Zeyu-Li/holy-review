# pynput API doesn't interact very well with VirtualBox :(
from pynput.keyboard import Key, Controller
from pyautogui import typewrite
import time

keyboard = Controller()

typings = """U0 Main()
{
	I64 i;
	for (i=0;i<64;i++) {
		MOV	RAX, '\\nThis '
		CALL	&PUT_CHARS
		MOV	RAX, 'isn\\'t '
		CALL	&PUT_CHARS
		MOV	RAX, 'your '
		CALL	&PUT_CHARS
		MOV	RAX, 'standard'
		CALL	&PUT_CHARS
		MOV	RAX, ' program'
		CALL	&PUT_CHARS
		MOV	RAX, 'ing lang'
		CALL	&PUT_CHARS
		MOV	RAX, 'uage\\n'
		CALL	&PUT_CHARS
	}
}

Main;

"""
# sleep seconds before starting
x = 3
# sleep for x seconds before starting
time.sleep(x)

keyboard.type(typings)