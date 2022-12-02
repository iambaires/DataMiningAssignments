package tests;
import org.junit.Test;
import org.junit.Assert.*;

import static org.junit.Assert.*;

public class PrimeTest {
    @Test
    public void test2() {
        Prime prime = new Prime();
        Boolean ans = prime.isPrime(2);
        assertEquals(true,ans);
    }
    @Test
    public void test3() {
        Prime prime = new Prime();
        Boolean ans = prime.isPrime(3);
        assertEquals(true,ans);
    }
    @Test
    public void test4() {
        Prime prime = new Prime();
        boolean ans = prime.isPrime(4);
        assertFalse(ans);
    }
    @Test
    public void test5() {
        Prime prime = new Prime();
        boolean ans = prime.isPrime(5);
        assertTrue(ans);
    }
    @Test
    public void test6() {
        Prime prime = new Prime();
        boolean ans = prime.isPrime(6);
        assertFalse(ans);
    }
}
