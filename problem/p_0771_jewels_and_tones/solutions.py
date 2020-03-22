from collections import Counter


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        stone_counter = Counter(S)

        num_of_jewels = sum([stone_counter.get(jewel_type, 0) for jewel_type in J])
        return num_of_jewels


class Solution2:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewel_counter = {jewel_type: 0 for jewel_type in J}

        for stone in S:
            if stone in jewel_counter:
                jewel_counter[stone] += 1
        return sum(jewel_counter.values())


class Solution3:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum([1 for stone in S if stone in J])
