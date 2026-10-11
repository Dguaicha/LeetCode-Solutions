class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:

        return (operations.count("X++") + operations.count("++X")) - (operations.count("--X") + operations.count("X--"))