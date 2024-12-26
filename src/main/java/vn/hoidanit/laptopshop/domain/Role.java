package vn.hoidanit.laptopshop.domain;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity

public class Role {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;
    private String name;
    private String depcription;

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDepcription() {
        return depcription;
    }

    public void setDepcription(String depcription) {
        this.depcription = depcription;
    }

    @Override
    public String toString() {
        return "Role [id=" + id + ", name=" + name + ", depcription=" + depcription + "]";
    }

}
