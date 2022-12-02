package hibernate;
import org.hibernate.*;
import org.hibernate.cfg.Configuration;



public class MainDeleteOrder {public static void main(String[] args) {

    SessionFactory factory = new Configuration()
            .configure("hibernate.cfg.xml")
            .addAnnotatedClass(Order.class)
            .addAnnotatedClass(Product.class)
            .buildSessionFactory();

    Session session = factory.getCurrentSession();

    try {
        session.beginTransaction();
        
        int orderID = 1;
        Order tempOrder = session.get(Order.class, orderID);

        System.out.println("\nLoaded order: " + tempOrder);
        System.out.println("Courses: " + tempOrder.getProducts());

        System.out.println("\nDeleting order: " + tempOrder);
        session.delete(tempOrder);

        session.getTransaction().commit();

        System.out.println("Done!");
    }
    finally {
    	
        session.close();
        factory.close();
    }
}
}
