class Solution:
    def toLowerCase(self, input_str: str) -> str:
        upper_a_ord = ord("A")
        upper_z_ord = ord("Z")
        upper_to_lower_offset = ord("a") - ord("A")

        result_chars = []
        for input_char in input_str:
            input_char_ord = ord(input_char)
            if upper_a_ord <= input_char_ord <= upper_z_ord:
                new_char = chr(input_char_ord + upper_to_lower_offset)
                result_chars.append(new_char)
            else:
                result_chars.append(input_char)
        return "".join(result_chars)
