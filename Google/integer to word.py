#Problem: Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
# Link: https://leetcode.com/problems/integer-to-english-words/



class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        def convert(num):
            if num == 0:
                return ""
            elif num < 10:
                return units[num] + " "
            elif num < 20:
                return teens[num - 10] + " "
            elif num < 100:
                return tens[num // 10] + " " + convert(num % 10)
            else:
                return units[num // 100] + " Hundred " + convert(num % 100)

        

        result = ""
        for i in range(len(thousands)):
            if num % 1000 != 0:
                result = convert(num % 1000) + thousands[i] + " " + result
            num //= 1000

        return result.strip()