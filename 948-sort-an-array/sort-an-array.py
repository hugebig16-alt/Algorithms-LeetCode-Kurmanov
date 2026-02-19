class Solution:
    def sortArray(self, nums):
        # Внутренняя функция для поддержания кучи
        def heapify(nums, n, i):
            largest = i  # предполагаем, что текущий элемент самый большой
            left = 2 * i + 1  # индекс левого ребёнка
            right = 2 * i + 2  # индекс правого ребёнка

            # если левый ребёнок больше текущего, меняем largest
            if left < n and nums[left] > nums[largest]:
                largest = left
            # если правый ребёнок больше, меняем largest
            if right < n and nums[right] > nums[largest]:
                largest = right

            # если самый большой не текущий, меняем их местами
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(nums, n, largest)  # повторно проверяем на поддереве

        n = len(nums)

        # Сначала строим max-кучу из массива
        for i in range(n // 2 - 1, -1, -1):
            heapify(nums, n, i)

        # Достаём элементы из кучи и ставим их в конец массива
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]  # переставляем максимум в конец
            heapify(nums, i, 0)  # восстанавливаем кучу для оставшейся части

        return nums  # возвращаем отсортированный массив
