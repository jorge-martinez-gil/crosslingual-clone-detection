import java.sql.*;
public Connection connectToDatabase(String url, String username, String password) throws SQLException {
    return DriverManager.getConnection(url, username, password);
}
