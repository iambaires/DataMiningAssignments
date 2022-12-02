package model.dataccess;

import java.sql.Connection;
import java.sql.SQLException;

public class MySQLConnection implements DatabaseConnection {

	@Override
	public Connection getDatabaseConnection() throws ClassNotFoundException, SQLException {
		return null;
	}
	
}
