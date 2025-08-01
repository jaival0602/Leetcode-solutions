# Last updated: 8/1/2025, 6:26:06 PM
class Solution:
    def defangIPaddr(self, address: str) -> str:
            return address.replace('.', '[.]')