## 1+2+3


def triangle_number(to):
	result = 0
	for i in range(1, to + 1):
		result = result + i

	return result


def divisible_by(x):
	res = []
	for i in range(1, x + 1):
		if x % i == 0:
			res.append(i)
	return res, len(res)


length = 0
i = 1
while length < 10:
	x = triangle_number(3)
	arr, length = divisible_by(x)
	print(arr)
	print(length)
	i += 1