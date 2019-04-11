/*
 * @lc app=leetcode id=146 lang=java
 *
 * [146] LRU Cache
 *
 * https://leetcode.com/problems/lru-cache/description/
 *
 * algorithms
 * Hard (24.40%)
 * Total Accepted:    278K
 * Total Submissions: 1.1M
 * Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
 *
 * 
 * Design and implement a data structure for Least Recently Used (LRU) cache.
 * It should support the following operations: get and put.
 * 
 * 
 * 
 * get(key) - Get the value (will always be positive) of the key if the key
 * exists in the cache, otherwise return -1.
 * put(key, value) - Set or insert the value if the key is not already present.
 * When the cache reached its capacity, it should invalidate the least recently
 * used item before inserting a new item.
 * 
 * 
 * Follow up:
 * Could you do both operations in O(1) time complexity?
 * 
 * Example:
 * 
 * 
 * 
 * cache.put(1, 1);
 * cache.put(2, 2);
 * cache.get(1);       // returns 1
 * cache.put(3, 3);    // evicts key 2
 * cache.get(2);       // returns -1 (not found)
 * cache.put(4, 4);    // evicts key 1
 * cache.get(1);       // returns -1 (not found)
 * cache.get(3);       // returns 3
 * cache.get(4);       // returns 4
 * 
 * 
 */
class CacheNode{
    public int key, val;
    public CacheNode next, prev;
    
    public CacheNode(int key, int val){
        this.key = key;
        this.val = val;
        this.next = null;
        this.prev = null;
    }
}
class LRUCache {
    private int size, capacity;
    private CacheNode head, tail;
    private Map<Integer, CacheNode> keyToNode;
    
    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.size = 0;
        this.keyToNode = new HashMap<Integer, CacheNode>();
        this.head = new CacheNode(0, 0);
        this.tail = new CacheNode(0, 0);
        this.head.next = this.tail;
        this.tail.prev = this.head;
    }
    
    private void pushback(CacheNode node){
        CacheNode lastNode = this.tail.prev;
        lastNode.next = node;
        node.prev = lastNode;
        node.next = this.tail;
        this.tail.prev = node;
    }
    
    private void deletenode(CacheNode node){
        CacheNode prevNode = node.prev;
        CacheNode nextNode = node.next;
        prevNode.next = nextNode;
        nextNode.prev = prevNode;
    }
    
    public int get(int key) {
        if(keyToNode.get(key) == null){
            return -1;
        }else{
            CacheNode node = keyToNode.get(key);
            int result = node.val;
            deletenode(node);
            pushback(node);
            return result;
        }
    }
    
    public void put(int key, int value) {
        if(keyToNode.get(key) != null){
            CacheNode node = keyToNode.get(key);
            node.val = value;
            deletenode(node);
            pushback(node);
        }else{
            CacheNode newNode = new CacheNode(key, value);
            keyToNode.put(key, newNode);
            pushback(newNode);
            //System.out.print(size);
            if(size == capacity){
                keyToNode.remove(head.next.key);
                deletenode(head.next);
            }else{
                size++;
            }
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */

