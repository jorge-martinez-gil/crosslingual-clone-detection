import javax.swing.*;
public class SimpleWindow {
    public static void createWindow() {
        JFrame frame = new JFrame("Simple Window");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(350, 200);
        frame.setVisible(true);
    }
}
