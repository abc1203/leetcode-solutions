class Solution(object):
    def maxUpgrades(self, count, upgrade, sell, money):
        """
        :type count: List[int]
        :type upgrade: List[int]
        :type sell: List[int]
        :type money: List[int]
        :rtype: List[int]

        for each center, check the number of upgrades when selling 0...n servers
        using bin search O(klogn)

        O(n) is possible by doing algebra to conclude
        maxUpgrade = ceil((count * upgrade - money) / (sell + upgrade))
        """

        def upgradeForCenter(count, upgrade, sell, money):
            res = 0
            l, r = 0, count
            while l < r:
                m = (l + r) / 2
                new_count = count - m
                new_money = money + sell * m
                upgraded = min(new_money / upgrade, new_count)
                res = max(res, upgraded)

                if upgraded == new_count:
                    r = m
                else:
                    l = m + 1
            return res
        
        n = len(count)
        ans = [0] * n
        for i in range(n):
            ans[i] = upgradeForCenter(count[i], upgrade[i], sell[i], money[i])
        return ans


            

        
