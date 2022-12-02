package model.business;

import java.sql.SQLException;

import model.dataccess.LoginDataAccess;
import model.entities.MessageException;
import model.entities.User;

public class LoginBusiness {
	
	private String username;
	private String password;
	private static LoginBusiness instance;
	
	
	private LoginBusiness(String username, String password) {
		this.username = username;
		this.password = password;
	}
	
	public static LoginBusiness getInstance(String username, String password) {
		if(instance == null) {
			instance = new LoginBusiness(username, password);
		}
		return instance;
	}
	
	public boolean verifyCredentials() throws ClassNotFoundException, SQLException {
		if (this.username.equals("")) {
			throw new MessageException("Username not informed.");
		} else if (password.equals("")) {
			throw new MessageException("Password not informed.");
		}
		
		User user = User.getInstance(this.username, this.password);
		
		return LoginDataAccess.getInstance().verifyCredentials(user);
	}
}
