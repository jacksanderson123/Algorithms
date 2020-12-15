def isPalindrome(string):
    # Write your code here.
	endPointer = len(string) - 1
	
	for i in range(len(string)):
    	if string[i] != string[endPointer]:
			return False
		endPointer -= 1
		if endPointer < i:
			return True
			

