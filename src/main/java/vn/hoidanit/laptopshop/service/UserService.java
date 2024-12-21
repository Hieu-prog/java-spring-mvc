package vn.hoidanit.laptopshop.service;

import java.util.List;

import org.springframework.stereotype.Service;
import vn.hoidanit.laptopshop.domain.User;
import vn.hoidanit.laptopshop.repository.UserRepository;

@Service
public class UserService {
    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public List<User> getAllUsers() {
        return this.userRepository.findAll();
    }

    public List<User> getAllUserByEmail(String email) {
        return this.userRepository.findOneByEmail(email);
    }

    public User getUserByID(long id) {
        return this.userRepository.findByid(id);
    }

    public User handleSaveUser(User user) {
        User eric = this.userRepository.save(user);
        System.out.println(eric);
        return eric;
    }

    public void deleteAUser(long id) {
        this.userRepository.deleteById(id);
    }

}
