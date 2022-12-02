package hibernate;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Entity
@Table(name="product")
public class Product {
	
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name="id")
    private int ID;
    
    @Column(name="name")
    private String name;

    @ManyToMany (cascade = {CascadeType.PERSIST})
    @JoinTable(
            name="order_detail",
            joinColumns =@JoinColumn(name="product_id"),
            inverseJoinColumns = @JoinColumn(name="order_id")
    )
    
    private List<Order> orders;
    
    public Product(){

    }
    
    public Product(String name){
        this.name = name;
    }
    
    public void addOrder(Order order) {

        if (orders == null) {
            orders = new ArrayList<Order>();
        }

        orders.add(order);
    }
    
    public List<Order> getOrders() {
        return orders;
    }
    
    public void setOrders(List<Order> orders) {
        this.orders = orders;
    }

    public int getID() {
        return ID;
    }
    
    public void setID(int ID) {
        this.ID = ID;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    
}
