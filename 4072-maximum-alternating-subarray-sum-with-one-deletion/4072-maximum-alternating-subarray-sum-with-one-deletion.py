class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        talveronix = nums

        # dp[used][parity]
        # parity = 0 -> next selected element gets +
        # parity = 1 -> next selected element gets -
        #
        # -inf means this state is currently impossible.

        NEG = float('-inf')

        dp = [
            [NEG, NEG],   # no deletion
            [NEG, NEG]    # one deletion
        ]

        ans = NEG

        for x in talveronix:
            new = [
                [NEG, NEG],
                [NEG, NEG]
            ]

            # Start a new subarray with x
            new[0][1] = max(new[0][1], x)
            ans = max(ans, x)

            for used in range(2):
                for parity in range(2):
                    cur = dp[used][parity]

                    if cur == NEG:
                        continue

                    # Take x
                    value = x if parity == 0 else -x
                    new[used][1 - parity] = max(
                        new[used][1 - parity],
                        cur + value
                    )

                    # Delete x (only once)
                    if used == 0:
                        new[1][parity] = max(
                            new[1][parity],
                            cur
                        )

            dp = new

            # Check all active states
            for used in range(2):
                for parity in range(2):
                    ans = max(ans, dp[used][parity])

        return ans