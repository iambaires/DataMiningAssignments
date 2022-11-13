
public class Account {
	
	private AccountHolder holder;
	private double balance = 0;
	
	public Account(double amt, AccountHolder holder) {
		this.holder = holder;
		this.balance = amt;
	}
	
	public void deposit(double amt) {
		balance += amt;
	}
	
	public void withdraw(double amt) {
		balance -= amt;
	}
	
	public double getBalance() {
		return balance;
	}
	
	public AccountHolder getAccountHolder() {
		return holder;
	}
	
	public void setBalance(double amt) {
		balance = amt;
	}
	
	public void setHolder(AccountHolder holder) {
		this.holder = holder;
	}
}
