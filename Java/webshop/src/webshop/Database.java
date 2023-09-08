package webshop;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

public class Database {
	
	Scanner sc = new Scanner(System.in);

	private static String jdbcUrl = "jdbc:mysql://localhost:3306/webshop";
	private static String username;
	private static String password;
	
	private Connection connection;
	private Statement statement;
	private ResultSet resultSet;
	private static boolean db_conn = false;
	
	public static void main(String[] args) throws SQLException {
		Database run = new Database();
		run.establish_connection();
		if(db_conn) {
			run.menu();
		}
		
		run.terminate_connection();
	}
	
	private void menu() {
		int choice = 0;
		System.out.println("\n1. List customers for specific product");
		System.out.println("2. List all products per category");
		System.out.println("3. List the best customers");
		System.out.println("4. List the best city");
		System.out.println("5. List the top 5 best sellers");
		System.out.println("6. Get annual sales report");
		
		choice = sc.nextInt();
		
		Questions q = new Questions();
		
		switch(choice) {
			case 1:
				q.choice_one(statement);
				break;
			case 2:
				q.choice_two(statement);
				break;
			case 3:
				q.choice_three(statement);
				break;
			case 4:
				q.choice_four(statement);
				break;
			case 5:
				q.choice_five(statement);
				break;
			case 6:
				q.choice_six(statement);
				break;
			default:
				System.out.println("No choice was made");
				break;
		}
		
	}
	
	private void terminate_connection() throws SQLException {
		if(resultSet != null) {
			resultSet.close();			
		}
		if(statement != null) {
			statement.close();			
		}
		if(connection != null) {
			connection.close();			
		}
		sc.close();
	}
	
	private void establish_connection() {
		try {
			System.out.println("Enter database username:");
			username = sc.nextLine();
			System.out.println("Enter database password:");
			password = sc.nextLine();
		} catch(Exception e) {
			e.printStackTrace();
		}
		
		try {
			connection = DriverManager.getConnection(jdbcUrl, username, password);
			statement = connection.createStatement();
			db_conn = true;
			System.out.println("Connection to database successful");
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}
}
