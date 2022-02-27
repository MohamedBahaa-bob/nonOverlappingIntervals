# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# correct solution but there's actually no need to pop any interval which takes O(n) and increase time complexity from
# O(nlogn) to O(n^2)
class Solution:
    """def eraseOverlapIntervals(self, intervals) -> int:
        intervals.sort()
        i, count = 0, 0
        print(intervals)
        while i < len(intervals) - 1:
            if intervals[i][1] > intervals[i + 1][0]:
                print(intervals[i + 1])
                if intervals[i][1] <= intervals[i + 1][1]:
                    intervals.pop(i + 1)
                else:
                    intervals.pop(i)
                count += 1
            else:
                i += 1
        return count"""
    def eraseOverlapIntervals(self, intervals) -> int:
        intervals.sort()
        count = 0
        print(intervals)
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            if prevEnd > intervals[i][0]:
                prevEnd = min(prevEnd, intervals[i][1])
                count += 1
            else:
                prevEnd = intervals[i][1]
        return count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()
    print(obj.eraseOverlapIntervals([[-52, 31], [-73, -26], [82, 97], [-65, -11], [-62, -49], [95, 99], [58, 95], [-31, 49], [66, 98], [-63, 2], [30, 47], [-40, -26]]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
