### Logic

1. Check if the given list is empty or not. The following code doesn't need to be processed.

2. Find the minimum number of strings from the list because prefixes can’t be longer than the string with the minimum length.

    e.g ["flower", "flow" , "flowest" ] -> "flow"

3. Set the string found in No. 2 above as an initial prefix.

    e.g [ "dog","racecar", "car"] -> "dog" is the initial prefix because the length is the minimum value.

4. Search a character from the beginning of the prefix one by one for each string, and if all strings have the same character in the same position, concatenate it to the answer.
