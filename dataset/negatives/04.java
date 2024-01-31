public void writeFile(String filename, String content) throws IOException {
    BufferedWriter writer = new BufferedWriter(new FileWriter(filename));
    writer.write(content);
    writer.close();
}