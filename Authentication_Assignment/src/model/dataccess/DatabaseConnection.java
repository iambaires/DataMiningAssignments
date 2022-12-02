package model.dataccess;

import java.sql.Connection;
import java.sql.SQLException;

public interface DatabaseConnection {
	public abstract Connection getDatabaseConnection() throws ClassNotFoundException, SQLException;
}
