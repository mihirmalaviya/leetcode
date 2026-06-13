class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        res = 0

        buckets=Counter(ages)

        for k1,c1 in buckets.items():
            for k2,c2 in buckets.items():
                if k2 <= 0.5 * k1 + 7 or k2 > k1:
                    continue

                if k1==k2:
                    res+=(c1-1)*c1
                else:
                    res+=c1*c2

        return res


"""

we are gonna do bucket sort into a hashmap

then for each key in that hashmap
 for each key in that hashmap
  if both are same then add (c1-1)*c1
  else if 1 can be friends with 2 add c1*c2

"""
