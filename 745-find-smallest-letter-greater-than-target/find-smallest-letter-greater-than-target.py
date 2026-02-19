class Solution:
    def nextGreatestLetter(self, letters, target):
        left = 0  # начало массива
        right = len(letters) - 1  # конец массива
        answer = None  # здесь будем хранить подходящую букву

        while left <= right:  # пока есть место для поиска
            mid = (left + right) // 2  # берём середину

            if letters[mid] > target:
                answer = letters[mid]  # нашли букву больше target, сохраняем её
                right = mid - 1  # продолжаем искать ещё меньшую подходящую букву слева
            else:
                left = mid + 1  # буква меньше или равна target, ищем справа

        # если подходящая буква найдена, возвращаем её
        # иначе возвращаем первую букву в массиве
        return answer if answer is not None else letters[0]
