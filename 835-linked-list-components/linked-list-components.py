class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        count = 0
        values = set(nums)

        while head:
            if head.val in values:
                if head.next is None or head.next.val not in values:
                    count += 1
            head = head.next

        return count