import java.io.*;
public void writeFile(String fileName, String content) throws IOException {
    BufferedWriter writer = new BufferedWriter(new FileWriter(fileName));
    writer.write(content);
    writer.close();
}