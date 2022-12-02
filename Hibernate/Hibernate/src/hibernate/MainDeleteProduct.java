package hibernate;
import org.hibernate.*;
import org.hibernate.cfg.Configuration;



public class MainDeleteProduct {public static void main(String[] args) {

    SessionFactory factory = new Configuration()
            .configure("hibernate.cfg.xml")
            .addAnnotatedClass(Order.class)
            .addAnnotatedClass(Product.class)
            .buildSessionFactory();

    Session session = factory.getCurrentSession();

    try {
        session.beginTransaction();
        
        int productId = 1;
        Product tempProduct = session.get(Product.class, productId);

        System.out.println("\nLoaded order: " + tempProduct);
        System.out.println("Courses: " + tempProduct.getOrders());

        System.out.println("\nDeleting order: " + tempProduct);
        session.delete(tempProduct);

        session.getTransaction().commit();

        System.out.println("Done!");
    }
    finally {
        session.close();
        factory.close();
    }
}
}
