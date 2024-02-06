# plus one 

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = False
        pointer =  len(digits) - 1
        while True:
            if pointer >= 0:
                digits[pointer] += 1
                carry = digits[pointer] >= 10
                digits[pointer] %= 10
                pointer -= 1
                if not carry:
                    break
            else:
                digits.insert(0, 1)
                break
        return digits
                
            