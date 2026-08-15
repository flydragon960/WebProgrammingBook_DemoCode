function validateForm() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    
    // Username validation: letters and digits only
    var usernameRegex = /^[A-Za-z0-9]+$/;
    if (!usernameRegex.test(username)) {
        alert('Username can only contain letters and digits.');
        return false;
    }
    
    // Password validation: at least 4 characters, at least one letter, and at least one digit
    var passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{4,}$/;
    if (!passwordRegex.test(password)) {
        alert('Password must be at least 4 characters long, including at least one letter and one digit.');
        return false;
    }
    
    return true;
}

