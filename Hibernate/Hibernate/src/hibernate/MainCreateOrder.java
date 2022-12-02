package hibernate;
import org.hibernate.*;
import org.hibernate.cfg.Configuration;

import java.util.Date;


public class MainCreateOrder {public static void main(String[] args) {

    SessionFactory factory = new Configuration()
            .configure("hibernate.cfg.xml")
            .addAnnotatedClass(Order.class)
            .addAnnotatedClass(Product.class)
            .buildSessionFactory();

    Session session = factory.getCurrentSession();

		try {
			session.beginTransaction();

			Date date = new Date();
			Order tempOrder = new Order("john", date);

			System.out.println("\nSaving the Order ...");
			session.save(tempOrder);
			System.out.println("Saved the order: " + tempOrder);

			Product tempProduct1 = new Product("product1");
			Product tempProduct2 = new Product("product2");

			tempOrder.addProduct(tempProduct1);
			tempOrder.addProduct(tempProduct2);

			System.out.println("\nSaving products ...");
			session.save(tempProduct1);
			session.save(tempProduct2);
			System.out.println("Saved products: " + tempOrder.getProducts());

			session.getTransaction().commit();

			System.out.println("Done!");
		}
		finally {
			
			session.close();
			factory.close();
		}
	}
}
