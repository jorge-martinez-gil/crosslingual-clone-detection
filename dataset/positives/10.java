public Map<Character, Integer> countChars(String str) {
    Map<Character, Integer> count = new HashMap<>();
    for (char c : str.toCharArray()) {
        count.put(c, count.getOrDefault(c, 0) + 1);
    }
    return count;
}
