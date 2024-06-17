const form = document.querySelector('#login')

form.addEventListener('submit', (e) => {
    e.preventDefault()

    let valid = true;

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    if (!validEmail(email) || !validPassword(password))
        valid = false

    if (valid)
        form.submit();
})

function validEmail(email) {
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
        alert("Invalid email address")
        return false;
    }
    return true
}

function validPassword(password) {
    if (password == 1234) {
        alert("Logado")
        return true
    }

    alert("Senha inválida")
    return false
  }