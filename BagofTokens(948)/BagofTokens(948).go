package BagofTokens

import (
	"math"
	"sort"
)

func bagOfTokensScore(tokens []int, power int) int {
	sort.Ints(tokens)

	l, r := 0, len(tokens)-1
	maxScore, score := 0, 0

	for l <= r {
		if power >= tokens[l] {
			score += 1
			power -= tokens[l]
			maxScore = int(math.Max(float64(maxScore), float64(score)))
			l += 1
		} else if score > 0 {
			score -= 1
			power += tokens[r]
			r -= 1
		} else {
			break
		}
	}

	return maxScore
}
