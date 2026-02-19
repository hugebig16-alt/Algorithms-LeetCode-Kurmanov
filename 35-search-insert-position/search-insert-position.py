class Solution:
    def searchInsert(self, nums, target):
        left = 0  # начало массива
        right = len(nums) - 1  # конец массива

        while left <= right:  # пока есть место для поиска
            mid = (left + right) // 2  # берём середину

            if nums[mid] == target:
                return mid  # нашли число, возвращаем его индекс
            elif nums[mid] < target:
                left = mid + 1  # число больше, ищем справа
            else:
                right = mid - 1  # число меньше, ищем слева

        return left  # число не найдено, возвращаем место, куда его можно вставить
