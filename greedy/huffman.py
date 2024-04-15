from math import ceil, log2

class Node:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, node):
        self.heap.append(node)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        parent = int((index - 1) / 2)
        if parent >= 0 and self.heap[parent].freq > self.heap[index].freq:
            # Swap
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.heapify_up(parent)

    def heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.heap) and self.heap[left].freq < self.heap[smallest].freq:
            smallest = left

        if right < len(self.heap) and self.heap[right].freq < self.heap[smallest].freq:
            smallest = right

        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.heapify_down(smallest)

    def extract_min(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)

        return root

    def build(self, data):
        for value, freq in data.items():
            self.insert(Node(value, freq))

        return self.heap

def build_huffman_tree(alphabet: dict[str, float]):
    n = len(alphabet)
    q = Heap()
    q.build(alphabet)

    for _ in range(1, n):
        x = q.extract_min()
        y = q.extract_min()
        z = Node(None, x.freq + y.freq)
        z.left = x
        z.right = y
        q.insert(z)

    return q.extract_min()

def build_huffman_codes(node: Node, prefix: str = ''):
    codes = {}

    if node is None:
        return codes

    if node.value is not None:
        codes[node.value] = prefix
        return codes

    codes.update(build_huffman_codes(node.left, prefix + '0'))
    codes.update(build_huffman_codes(node.right, prefix + '1'))
    return codes

def build_alphabet(text: str):
    alphabet = {}
    for char in text:
        if char in alphabet:
            alphabet[char] += 1
        else:
            alphabet[char] = 1

    return alphabet

def huffman_encode(text: str, codes: dict[chr, str]):
    return ''.join([ codes[char] for char in text ])

def huffman_decode(encoded_text: str, tree: Node):
    decoded_text = ''
    node = tree

    for bit in encoded_text:
        if bit == '0':
            node = node.left
        else:
            node = node.right

        if node.value is not None:
            decoded_text += node.value
            node = tree

    return decoded_text

text_sample = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat. Duis semper. Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. Pellentesque congue. Ut in risus volutpat libero pharetra tempor. Cras vestibulum bibendum augue. Praesent egestas leo in pede. Praesent blandit odio eu enim. Pellentesque sed dui ut augue blandit sodales. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aliquam nibh. Mauris ac mauris sed pede pellentesque fermentum. Maecenas adipiscing ante non diam sodales hendrerit.'

alphabet = build_alphabet(text_sample)
huffman_tree = build_huffman_tree(alphabet)
huffman_codes = build_huffman_codes(huffman_tree)
encoded = huffman_encode(text_sample, huffman_codes)
print(encoded)
decoded = huffman_decode(encoded, huffman_tree)
print(decoded)
