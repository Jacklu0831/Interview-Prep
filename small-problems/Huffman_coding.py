"""

A Huffman code is a type of optimal prefix code that is used for compressing data. 
The Huffman encoding and decoding schema is also lossless, 
meaning that when compressing the data to make it smaller, there is no loss of information.

The Huffman algorithm works by assigning codes that correspond to the relative frequency of each 
character for each character. The Huffman code can be of any length and does not require a prefix; 
therefore, this binary code can be visualized on a binary tree with each encoded character being 
stored on leafs.

There are many types of pseudocode for this algorithm. At the basic core, it is comprised of 
building a Huffman tree, encoding the data, and, lastly, decoding the data.

Here is one type of pseudocode for this coding schema:

- Take a string and determine the relevant frequencies of the characters.
- Build and sort a list of tuples from lowest to highest frequencies.
- Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the
  more frequent letters. (This is the heart of the Huffman algorithm.)
- Trim the Huffman Tree (remove the frequencies from the previously built tree).
- Encode the text into its compressed form.
- Decode the text from its compressed form.A Huffman code is a type of optimal prefix code that is 
  used for compressing data. The Huffman encoding and decoding schema is also lossless, 
  meaning that when compressing the data to make it smaller, there is no loss of information.

Learned from: http://bhrigu.me/blog/2017/01/17/huffman-coding-python-implementation/
Awesome video: https://www.youtube.com/watch?v=dM6us854Jk0
"""

import os
from heapq import heappush, heappop

class Heap_Node:
    # freq is the main "data" that the heap nodes hold
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right


    def cmp(self, other):
        if (not other) or (not isinstance(other, Heap_Node)):
            return -1
        return self.freq > other.freq


class Huffman_Coding:

    def __init__(self, path):
        self.path = path
        self.heap = []
        self.code = {}
        self.reverse_mapping = {} # for decoding


# ====================================
# Functions for compression start here
# ====================================


    def get_frequency_dict(self, text):
        freq_dict = {}
        for ch in text:
            freq_dict[ch] = freq_dict.get(ch, 0) + 1
        return freq_dict


    def get_heap(self, freq_dict):
        for ch, freq in freq_dict.items():
            heappush(self.heap, Heap_Node(ch, freq))


    def merge_nodes(self):
        while len(self.heap) >= 2:
            node1 = heappop(self.heap)
            node2 = heappop(self.heap)

            # can use char==None bool to check whether we reach a node
            merged = Heap_Node(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heappush(self.heap, merged)


    def _get_codes(self, root, curr_code):
        if not root:
            return

        if root.char != None:
            self.codes[root.char] = curr_code
            self.reverse_mapping[curr_code] = root.char
            return

        # binary 1 represents right and 0 for left
        self._get_codes(root.left, curr_code + "0")
        self._get_codes(root.right, curr_code + "1")


    def get_codes(self):
        root = heappop(self.heap)
        curr_code = ""
        self._get_codes(root, curr_code)


    def get_encoded_text(self, text):
        encoded_text = ""
        for ch in text:
            encoded_text += self.codes[ch]
        return encoded_text


    def pad_encoded_text(self, encoded_text):
        # for creating byte array
        padding = 8 - len(encoded_text) % 8
        encoded_text += "0" * padding

        # padding info is used for decompression
        padding_info = "{0:08b}".format(padding)
        encoded_text = padding_info + encoded_text
        return encoded_text


    def get_byte_array(self, padded_encoded_text):
        b_array = byteArray()
        for i in range(0, len(padded_encoded_text), 8):
            b_array.append(int(padded_encoded_text[i:i+8], 2))

        return b_array


    def compress(self):
        filename, _ = os.path.splitext(self.path)
        output_path = filename + ".bin"

        with open(self.path, "r") as f, open(output_path, "wb") as output:
            text = f.read()
            text = text.rstrip() # strip whitespaces

            freq_dict = self.get_frequency_dict(text)
            self.get_heap(freq_dict)
            self.merge_nodes()
            self.get_codes()

            encoded_text = self.get_encoded_text(text)
            padded_encoded_text = self.pad_encoded_text(encoded_text)
            b_array = get_byte_array(padded_encoded_text)

            output.write(bytes(b_array))

        print("Done Compression.")
        return output_path


# ======================================
# Functions for decompression start here
# ======================================


    def remove_padding(self, padded_encoded_text):
        padded_info = padded_encoded_text[:8]
        padding = int(padded_info, 2)
        print(padding)
        print(type(padding))

        encoded_text = padded_encoded_text[8:][:-1*padding]
        return encoded_text


    def decode_text(self, encoded_text):
        # if code not found in reverse_mapping, concatenate the next
        curr_code = ""
        decoded_text = ""

        for bit in encoded_text:
            curr_code += bit
            if curr_code in self.reverse_mapping:
                ch = self.reverse_mapping[curr_code]
                decoded_text += ch
                curr_code = ""

        return decoded_text


    def decompress(self, input_path):
        filename, _ = os.path.splitext(self.path)
        output_path = filename + "_decompressed" + ".txt"

        with open(input_path, "rb") as f, open(output_path, "w") as output:
            bit_str = ""

            byte = f.read(1)
            while(byte != ""):
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_str+= bits
                byte = f.read(1)

            encoded_text = remove_padding(bit_str)
            decompressed_text = self.decode_text(encoded_text)
            output.write(decompressed_text)

        print("Done Decompression.")
        return output_path


input_path = "test_random_file.txt"
h = Huffman_Coding(input_path)
output_path = h.compress()
h.decompress(output_path)









