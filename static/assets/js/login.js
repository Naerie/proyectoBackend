let intentos = 4; // número máximo de intentos

function validar(event) {
    event.preventDefault(); // evita que el formulario se envíe

    let email = document.getElementById('email').value;
    let passwd = document.getElementById('password').value;

    if (email === 'admin@gmail.com' && passwd === '123456') {
        console.log('Inicio de sesión exitoso.');
        window.location.href = "/manage/";
    } else {
        intentos--; 
        if (intentos > 0) {
            alert(`Contraseña o correo inválido. Te quedan ${intentos} intentos.`);
        } else {
            alert('Has excedido el número de intentos.');
            document.getElementById('email').disabled = true;
            document.getElementById('password').disabled = true;
            document.getElementById('btnLogin').disabled = true;
        }
    }
}

