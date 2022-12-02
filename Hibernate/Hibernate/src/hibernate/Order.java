package hibernate;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;


@Entity
@Table(name="\"order\"")
public class Order {
	
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name="id")
    private int ID;
    
    @Column(name="date")
    private Date date;
    
    @Column(name="customer_name")
    private String customerName;

    @ManyToMany (cascade = {CascadeType.PERSIST})
    @JoinTable(
            name="order_detail",
            joinColumns =@JoinColumn(name="order_id"),
            inverseJoinColumns = @JoinColumn(name="product_id")
    )
    
    private List<Product> products;

    public Order() {

    }
    
    public Order(String customerName, Date date) {
        this.date = date;
        this.customerName = customerName;
    }

    public void addProduct(Product product) {

        if (products == null) {
            products = new ArrayList<Product>();
        }

        products.add(product);
    }
    
    public List<Product> getProducts() {
        return products;
    }
    
    public int getID() {
        return ID;
    }

    public void setID(int ID) {
        this.ID = ID;
    }
    
    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }
    
    public String getCustomerName() {
        return customerName;
    }

    public void setCustomerName(String customerName) {
        this.customerName = customerName;
    }

}
