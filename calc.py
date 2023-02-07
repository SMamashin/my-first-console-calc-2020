import datetime

what = str(input('Что делаем?'))

def main():
	global what
	print('[Calc in Console]: Success download!')
	print('+ - * /')
	if what == "+":
		num1 = int(input('Введите первое число: '))
		num2 = int(input('Введите второе число: '))
		result_plus = str(num1 + num2)
		print('Результат сложения: ' + result_plus)

	elif what == "-":
		num3 = int(input('Введите первое число: '))
		num4 = int(input('Введите второе число: '))
		result_min = str(num3 - num4)
		print('Результат вычитания: ' + result_min)

	elif what == "*":
		num5 = int(input('Введите первое число: '))
		num6 = int(input('Введите второе число: '))
		result_um = str(num5 * num6)
		print('Результат умножения: ' + result_um)

	elif what == ['/', '//']:
		num7 = int(input('Введите первое число: '))
		num8 = int(input('Введите второе число: '))
		result_del = str(num7 // num8)
		print('Результат деления: ' + result_del)

	elif what == "/commands":
		print('+ - * //')
		print('time')
	elif what == ['time', '/time']:
		local_datetime = datetime.datetime.now()
		print('Время(time): ' + local_datetime)

	else:
		print('Неизвестная команда!')
		print('Список моих комманд: /commands')
while True:
	main()