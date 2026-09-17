class Solution:
    def __init__(self):
        # List to store each string and its length as tuples
        self.encoded_list = []

    def encode(self, strs: List[str]) -> str:
        # Clear the encoded list before encoding
        self.encoded_list.clear()
        encoded_string = ""
        
        # Append each string and its length as a tuple to the list
        for word in strs:
            self.encoded_list.append((word, len(word)))
            encoded_string += word  # Concatenate all strings together
        
        print("Encoded List with Lengths:", self.encoded_list)
        print("Encoded String:", encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        pos = 0
        
        # Reconstruct each word using the lengths stored in encoded_list
        for word, length in self.encoded_list:
            decoded_word = s[pos:pos + length]
            decoded_list.append(decoded_word)
            pos += length  # Move the position by the length of the word
        
        print("Decoded List:", decoded_list)
        return decoded_list
