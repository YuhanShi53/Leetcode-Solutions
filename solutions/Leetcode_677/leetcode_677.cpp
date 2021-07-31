#include <string>
#include <unordered_map>

struct TrieNode
{
public:
    TrieNode* child[26] = {};
    int val = 0;
};

class MapSum {
public:
    TrieNode root;
    std::unordered_map<std::string, int> dict;

    MapSum() {}
    
    void insert(std::string key, int val) {
        int diff = val - dict[key];
        dict[key] = val;
        TrieNode* current = &root;
        for (char x : key) {
            x -= 'a';
            if (current->child[x] == nullptr)
                current->child[x] = new TrieNode();
            current = current->child[x];
            current->val += diff;
        }
    }
    
    int sum(std::string prefix) {
        TrieNode* current = &root;
        for (char x : prefix) {
            x -= 'a';
            if (current->child[x] == nullptr)
                return 0;
            current = current->child[x];
        }
        return current->val;
    }
};