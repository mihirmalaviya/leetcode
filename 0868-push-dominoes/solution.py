class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = ["L"] + list(dominoes) + ["R"]
        l = 0

        for r in range(1, len(dominoes)):
            if dominoes[r] == ".":
                continue

            dist = r - l - 1

            if dist > 0:
                if dominoes[l] == dominoes[r]:
                    for i in range(l + 1, r):
                        dominoes[i] = dominoes[l]

                elif dominoes[l] == "R" and dominoes[r] == "L":
                    for i in range(1, (dist // 2) + 1):
                        dominoes[l + i] = "R"
                        dominoes[r - i] = "L"

            l = r

        return "".join(dominoes[1:-1])

