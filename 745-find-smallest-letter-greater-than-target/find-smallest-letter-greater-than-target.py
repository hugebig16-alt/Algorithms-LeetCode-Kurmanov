class Solution:
    def nextGreatestLetter(self, letters, target):
        left, right = 0, len(letters) - 1
        answer = None

        while left <= right:
            mid = (left + right) // 2

            if letters[mid] > target:
                answer = letters[mid]
                right = mid - 1   # ищем меньший, но всё ещё > target
            else:
                left = mid + 1

        return answer if answer is not None else letters[0]
