class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # idea: area of 1st rectangle adds the area of 2nd then minus the overlapped area

        # area of both recs
        area_1 = (ax2 - ax1) * (ay2 - ay1)
        area_2 = (bx2 - bx1) * (by2 - by1)

        # overlapped area
        length = min(ax2, bx2) - max(ax1, bx1)
        height = min(ay2, by2) - max(ay1, by1)
        area_ol = length * height if length > 0 and height > 0 else 0

        return area_1 + area_2 - area_ol
