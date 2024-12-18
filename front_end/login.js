document.getElementById("login-form").
addEventListener("submit", handleLoginSubmit);

// Fonction pour gérer la soumission du formulaire de connexion
async function handleLoginSubmit(event) {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    console.log("Form submitted");

    if (!username || !password) {
        alert("Veuillez remplir tous les champs.");
        return;
    }

    try {
        const response = await sendLoginRequest(username, password);
        const data = await response.json();

        if (response.ok) {
            handleLoginSuccess(data);
        } else {
            handleLoginError(data);
        }
    } catch (error) {
        handleNetworkError(error);
    }
}

// Envoie la requête de connexion au serveur
async function sendLoginRequest(username, password) {
    const url = "http://127.0.0.1:8090/token";
    const body = `username=${username}&password=${password}`;

    return await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: body,
    });
}

// Gère la réussite de la connexion
function handleLoginSuccess(data) {
    Swal.fire({
        title: 'Connexion réussie !',
        icon: 'success',
        confirmButtonText: 'OK',
    }).then((result) => {
        if (result.isConfirmed) {
            localStorage.setItem("token", data.access_token);
            window.location.replace(`inventory.html?id_compte=${data.id_compte}`);
        }
    });
}

// Gère l'erreur lors de la connexion
function handleLoginError(data) {
    Swal.fire({
        title: 'Oups, erreur !',
        text: data?.detail || "Erreur inconnue",
        icon: 'error',
        confirmButtonText: 'OK',
    });
}

// Gère les erreurs réseau ou autres
function handleNetworkError(error) {
    console.error("Erreur réseau :", error);
    Swal.fire({
        title: 'Erreur réseau',
        text: 'Veuillez réessayer plus tard.',
        icon: 'error',
        confirmButtonText: 'OK',
    });
}
