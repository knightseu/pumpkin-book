# root node will have a value "*", and it will never be empty
class TrieNode:
  def __init__(self, char: str):
    self.char =  char
    # list of TrieNode
    self.children = []
    self.isWord = False
    self.counter = 1

def add_trie_node(root: TrieNode, word: str):
  node = root
  for char in word:
    found_in_children = False

    for child in node.children:
      if child.char == char:
        child.counter += 1
        node = child
        found_in_children = True
        break
    if not found_in_children:
      new_node = TrieNode(char)
      node.children.append(new_node)
      node = new_node
  if not node == root:
    node.isWord = True

def find_in_trie(root, prefix: str):
  node = root
  if not root.children:
    return False

  for char in prefix:
    found = False
    for child in node.children:
      if child.char == char:
        found = True
        node = child
        break
    if not found:
      return False
  return node.isWord

if __name__ == "__main__":
    root = TrieNode('*')
    add_trie_node(root, "hackathon")
    add_trie_node(root, 'hack')

    print(find_in_trie(root, 'hac'))
    print(find_in_trie(root, 'hack'))
    print(find_in_trie(root, 'hackathon'))
    print(find_in_trie(root, 'ha'))
    print(find_in_trie(root, 'hammer'))