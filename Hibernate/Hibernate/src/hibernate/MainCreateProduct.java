package hibernate;
import org.hibernate.*;
import org.hibernate.cfg.Configuration;

import java.util.Date;


public class MainCreateProduct {public static void main(String[] args) {

    SessionFactory factory = new Configuration()
            .configure("hibernate.cfg.xml")
            .addAnnotatedClass(Order.class)
            .addAnnotatedClass(Product.class)
            .buildSessionFactory();

    Session session = factory.getCurrentSession();

    try {
        session.beginTransaction();

        Date date = new Date();
        Product tempProduct = new Product("product1");

        System.out.println("\nSaving the Product ...");
        session.save(tempProduct);
        System.out.println("Saved the product: " + tempProduct);

        Order tempOrder1 = new Order("john", date);
        Order tempOrder2 = new Order("jane", date);

        tempProduct.addOrder(tempOrder1);
        tempProduct.addOrder(tempOrder2);

        System.out.println("\nSaving orders ...");
        session.save(tempOrder1);
        session.save(tempOrder2);
        System.out.println("Saved orders: " + tempProduct.getOrders());

        session.getTransaction().commit();

        System.out.println("Done!");
    }
    finally {
        session.close();
        factory.close();
    }
}
}
