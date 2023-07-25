class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = {}

        for letter in magazine:
            if not magazine_dict.get(letter):
                magazine_dict[letter] = 1
            else:
                magazine_dict[letter] += 1

        for letter in ransomNote:
            if letter not in magazine_dict: 
                return False
            elif magazine_dict[letter] == 0:
                return False
            else:
                magazine_dict[letter] -= 1

        return True