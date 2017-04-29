package ca3.guitarstockapp;

/**
 * Created by garet on 30/04/2017.
 */

public class Guitar {

    public int ID;
    public boolean IsNew;
    public String Name;
    public int Stock;

    public Guitar(int ID, boolean isNew, String make, String name, int stock) {
        this.ID = ID;
        IsNew = isNew;
        Make = make;
        Name = name;
        Stock = stock;
    }

    public String Make;

    public int getID() {
        return ID;
    }

    public void setID(int ID) {
        this.ID = ID;
    }

    public boolean isNew() {
        return IsNew;
    }

    public void setNew(boolean aNew) {
        IsNew = aNew;
    }

    public String getMake() {
        return Make;
    }

    public void setMake(String make) {
        Make = make;
    }

    public String getName() {
        return Name;
    }

    public void setName(String name) {
        Name = name;
    }

    public int getStock() {
        return Stock;
    }

    public void setStock(int stock) {
        Stock = stock;
    }
}
