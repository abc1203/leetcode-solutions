class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str

        numbers that need to be mapped:
        0-20, 30, 40, 50, 60, 70, 80, 90, 100, 1000, 1000000, 1000000000
        """

        mapping = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            100: "Hundred",
            1000: "Thousand",
            1000000: "Million",
            1000000000: "Billion"
        }

        if num == 0: return "Zero"

        lisOfNums = mapping.keys()
        lisOfNums.sort(reverse=True)

        def convert(num):
            ans = ""
            for n in lisOfNums:
                resDigit = num // n
                if resDigit > 1:
                    ans += convert(resDigit) + " "
                    ans += mapping[n] + " "
                elif resDigit == 1:
                    if num >= 100: ans += convert(resDigit) + " "
                    ans += mapping[n] + " "
                num %= n
            return ans.strip()

        return convert(num)





        
