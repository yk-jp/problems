package LongestCommonPrefix

func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}

	minStrAt := 0

	for idx, str := range strs {
		if len(str) < len(strs[minStrAt]) {
			minStrAt = idx
		}
	}

	minStr := strs[minStrAt]
	commonPrefix := ""

	for i := 0; i < len(minStr); i++ {
		for j := 0; j < len(strs); j++ {
			if minStr[i] != strs[j][i] {
				return commonPrefix
			}
		}
		commonPrefix += string(minStr[i])
	}

	return commonPrefix
}
