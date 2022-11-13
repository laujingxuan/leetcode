package leetcode;

import java.util.*;

public class TopKFrequentHeap {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(topKFrequent(new String[]{"i","love","leetcode","i","love","coding"}, 2).toArray()));
        System.out.println(Arrays.toString(topKFrequentWithMaxHeap(new String[]{"i","love","leetcode","i","love","coding"}, 2).toArray()));
    }

    //Time Complexity: O(nlogn + Klogn) = O(nlogn)
    //Space Complexity: O(n), for heap
    public static List<String> topKFrequentWithMaxHeap(String[] words, int k) {
        Map<String, Integer> map = new HashMap<>();
        for(String word:words){
            map.put(word, map.getOrDefault(word, 0)+1);
        }
        PriorityQueue<Map.Entry<String, Integer>> pq = new PriorityQueue<>(new MyComparator());
        for(Map.Entry<String, Integer> e:map.entrySet()){
            pq.offer(e);
        }
        List<String> ans = new LinkedList<>();
        for(int i = 0;i<=k-1;i++){
            ans.add(pq.poll().getKey());
        }
        return ans;
    }

    static class MyComparator implements Comparator<Map.Entry<String, Integer>> {
        public int compare(Map.Entry<String, Integer> e1, Map.Entry<String, Integer> e2){
            String word1 = e1.getKey();
            int freq1 = e1.getValue();
            String word2 = e2.getKey();
            int freq2 = e2.getValue();
            if(freq1!=freq2){
                return freq2-freq1;
            }
            else {
                return word1.compareTo(word2);
            }
        }
    }

    //bad implementation as time complexity around N^2 logN since sorting was carried out multiple times
    //beside space complexity also bad as at least 2 hashmap and 2 list are used.
    public static List<String> topKFrequent(String[] words, int k) {
        HashMap<String, Integer> checkMap = new HashMap<>();
        for (int i = 0; i < words.length; i++){
            if (checkMap.containsKey(words[i])){
                int value = checkMap.get(words[i]);
                checkMap.put(words[i], value+1);
            }else{
                checkMap.put(words[i], 1);
            }
        }
        HashMap<Integer, List<String>>valueCheck = new HashMap<>();
        List<Integer> integerCheck = new ArrayList<>();
        for (String key:checkMap.keySet()){
            if (valueCheck.containsKey(checkMap.get(key))){
                List<String> foundList = valueCheck.get(checkMap.get(key));
                foundList.add(key);
                valueCheck.put(checkMap.get(key), foundList);
            }else{
                List<String>newList = new ArrayList<>();
                newList.add(key);
                valueCheck.put(checkMap.get(key), newList);
                integerCheck.add(checkMap.get(key));
            }
        }
        Collections.sort(integerCheck, Collections.reverseOrder());
        List<String> toReturnList = new ArrayList<>();
        while (k != 0){
            int currentMaxCount = integerCheck.get(0);
            List<String>currentStringList = valueCheck.get(currentMaxCount);
            Collections.sort(currentStringList);
            integerCheck.remove(0);
            while (currentStringList.size() != 0 && k != 0){
                String word = currentStringList.get(0);
                toReturnList.add(word);
                currentStringList.remove(0);
                k--;
            }
        }
        return toReturnList;
    }
}
