package model.dataccess;

import java.sql.Connection;
import java.sql.SQLException;

public class ConnectionFactory {
	public Connection getConnection(String dbName) throws ClassNotFoundException, SQLException {
		if(dbName.equals("postgres")) {
			return new PostgresConnection().getDatabaseConnection();
		}
		
		return new MySQLConnection().getDatabaseConnection();
	}
}
