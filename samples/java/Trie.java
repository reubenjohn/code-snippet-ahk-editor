
    static class Trie {
        char val;
        Map<Character, Trie> children = new HashMap<>();
        Trie(char val) {
            this.val = val;
        }
        public String toString() {
            return String.format("%s", children);
        }
        Trie add(Trie node) {
            children.put(node.val, node);
            return node;
        }
        Trie get(Character val) {
            return children.get(val);
        }
    }
