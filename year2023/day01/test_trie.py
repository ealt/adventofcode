from trie import Trie


def test_prefix():
    trie = Trie(["aaa", "aba", "c"])
    assert trie.first_prefix("aaaba") == "aaa"
    assert trie.first_prefix("abc") == ""
    assert trie.first_prefix("aba") == "aba"
