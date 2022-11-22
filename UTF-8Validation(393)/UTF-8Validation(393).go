package UTF8Validation

func validUtf8(data []int) bool {
	numOfByte := 0
	i := 0

	for i < len(data) {
		numOfByte = countByte(data[i])
		if numOfByte == 1 || numOfByte > 4 {
			return false
		}
		if numOfByte == 0 {
			i += 1
			continue
		}
		numOfByte -= 1
		i += 1

		for i < len(data) {
			nextNumOfByte := countByte(data[i])
			if nextNumOfByte != 1 {
				return false
			}

			numOfByte -= 1

			if numOfByte == 0 {
				i += 1
				break
			}
			i += 1
		}
	}

	return numOfByte == 0
}

func countByte(num int) int {
	count := 0
	for i := 7; i >= 0; i-- {
		if num&(1<<i) > 0 {
			count += 1
		} else {
			break
		}
	}
	return count
}
