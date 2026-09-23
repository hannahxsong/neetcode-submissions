class Solution:
    def calPoints(self, operations: List[str]) -> int:

        count = 0
        total_score = []
        for score in operations:
            # check for "+"
            if score == "+":
                total_score.append(total_score[-1] + total_score[-2])
            # check for "D"
            elif score == "D":
                total_score.append(2 * total_score[-1])
            # check for "C"
            elif score == "C":
                total_score.pop()
            # check for ints x
            else:
                total_score.append(int(score))
        
        for i in total_score:
            count += i

        return count
