import java.util.Random;
public int generateRandomNumber(int upperBound) {
    Random random = new Random();
    return random.nextInt(upperBound);
}
