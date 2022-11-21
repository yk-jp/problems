### Logic

1. Sort the given list in ascending order because we want to subtract the smallest token from the current power and add the maximum power when the score is decreased.

2. Use two pointers to keep track of the current position where we should use a token to count up the score and get power when the power is not enough.

3. Keep going until we finish searching all elements in the list or score became less than 0. Update the maximum score when the score counts up as we don’t need to play all tokens.

   conditions
   <br>
    1. When we have enough power to play a token(power is greater than or equal to a token),
       score counts up and update the left pointer and maximum score.
    2. If not, we need to check if the score is more than 0, because we can consume one point to get power from a token.
    3. Apart from these conditions, we can't play anymore, that means game ends and return result

4. return result