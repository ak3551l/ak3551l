package bank;

class Account  {
    public String name;
    protected String email;
    private String password;

    // getters & setters
    public String getPassword() {
        return this.password;
    }

    // setters
    public void setPassword(String pass) {
        this.password = pass;
    }

}
public class Bank {
    //we make main class public for accessible
    public static void main(String args[]) {
        Account account1 = new Account();
        account1.name = "Apna College";
        account1.email = "apnacollege@gmail.com";
        account1.setPassword("abcd");
        System.out.println(account1.getPassword());

    }
}
