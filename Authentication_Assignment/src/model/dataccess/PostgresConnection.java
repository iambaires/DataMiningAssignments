package model.dataccess;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class PostgresConnection implements DatabaseConnection {

	@Override
	public Connection getDatabaseConnection() throws ClassNotFoundException, SQLException {
		final String URL = "jdbc:postgresql://localhost:5432/postgres";

		final String USER = "postgres";

		final String PWD = "123";

		Class.forName("org.postgresql.Driver");
		
		return DriverManager.getConnection(URL, USER, PWD);
	}

}
