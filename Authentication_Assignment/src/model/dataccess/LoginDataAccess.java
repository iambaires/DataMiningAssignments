package model.dataccess;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import model.entities.User;

public class LoginDataAccess {
	
	private static LoginDataAccess instance = new LoginDataAccess();
	
	LoginDataAccess() {
		
	}
	
	public Boolean verifyCredentials(User user) throws ClassNotFoundException, SQLException {

		final String dbName = "postgres";

		ConnectionFactory connectionFactory = new ConnectionFactory();
		
		Connection connection = connectionFactory.getConnection(dbName);

		final PreparedStatement stmt = connection.prepareStatement("SELECT * FROM users WHERE username=? and password=?");

		stmt.setString(1, user.getUserName());
		stmt.setString(2, user.getPassword());

		ResultSet rs = stmt.executeQuery();

		return rs.next();
		
	}
	
	public static LoginDataAccess getInstance() {
		return instance;
	}

}

