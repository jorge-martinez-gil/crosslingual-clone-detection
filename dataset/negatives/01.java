public String readFile(String filename) throws IOException {
    BufferedReader reader = new BufferedReader(new FileReader(filename));
    StringBuilder stringBuilder = new StringBuilder();
    String line;
    while ((line = reader.readLine()) != null) {
        stringBuilder.append(line).append("\n");
    }
    reader.close();
    return stringBuilder.toString();
}