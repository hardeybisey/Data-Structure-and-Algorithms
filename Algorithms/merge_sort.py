class MergeSort:
    def split_arr(self, array):
        if len(array) ==1:
            return array
        length = len(array)
        mid = length // 2
        left = array[:mid]
        right = array[mid:]
        # print('left: ' , left,'right: ' , right)
        return self.merge_sort(self.split_arr(left), self.split_arr(right))

    def merge_sort(self, left, right):
        # print('merge left: ' , left,'merge right: ' , right)
        result = []
        leftidx = 0
        rightidx= 0
        while leftidx < len(left) and rightidx < len(right):
            if left[leftidx] < right[rightidx]:
                result.append(left[leftidx])
                leftidx += 1
            else:
                result.append(right[rightidx])
                rightidx += 1
        # print('result: ',result + left[leftidx:] + right[rightidx:])
        return result + left[leftidx:] + right[rightidx:]
    
n = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
a = MergeSort()
a.split_arr(n)