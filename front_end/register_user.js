document.addEventListener("DOMContentLoaded", initializeForm);

// Initialisation des événements après le chargement du DOM
function initializeForm() {
    const registerForm = document.getElementById("register-form");

    if (!registerForm) {
        console.error("Formulaire d'inscription introuvable dans le DOM.");
        return;
    }

    registerForm.addEventListener("submit", handleFormSubmit);
}

// Fonction pour gérer la soumission du formulaire
async function handleFormSubmit(event) {
    event.preventDefault();

    const formData = collectFormData();

    if (!formData) {
        alert("Veuillez remplir tous les champs obligatoires et sélectionner un fichier.");
        return;
    }

    try {
        const response = await submitForm(formData);

        if (response.ok) {
            const data = await response.json();
            console.log("Réponse serveur :", data);
            alert("Inscription réussie !");
            redirectToProfile(data.id_compte);
        } else {
            await handleError(response);
        }
    } catch (error) {
        console.error("Erreur réseau ou serveur :", error);
        alert("Impossible de se connecter au serveur.");
    }
}

// Collecte les données du formulaire en validant les champs obligatoires
function collectFormData() {
    const prenom = document.getElementById("first-name")?.value;
    const nom = document.getElementById("last-name")?.value;
    const adresse = document.getElementById("address")?.value;
    const fileInput = document.getElementById("file");
    const file = fileInput?.files[0];

    if (!prenom || !nom || !adresse || !file) {
        console.error("Tous les champs obligatoires ne sont pas remplis ou le fichier est manquant.");
        return null;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("nom", nom);
    formData.append("prenom", prenom);
    formData.append("addresse", adresse);
    formData.append("score", 0); // Valeur par défaut
    formData.append("niveau", 0); // Valeur par défaut
    formData.append("avatar", file);

    return formData;
}

// Envoie le formulaire au serveur via une requête POST
async function submitForm(formData) {
    const SERVER_URL = "http://127.0.0.1:8090/compte";
    return await fetch(SERVER_URL, {
        method: "POST",
        body: formData,
    });
}

// Gère les erreurs de réponse du serveur
async function handleError(response) {
    let errorMessage = "Erreur lors de l'inscription. Veuillez réessayer.";

    try {
        const errorData = await response.json();
        errorMessage = errorData.detail || errorMessage;
    } catch (error) {
        console.error("Impossible d'analyser le message d'erreur du serveur :", error);
    }

    console.error("Erreur serveur :", response.status, errorMessage);
    alert(errorMessage);
}

// Redirige vers la page de profil avec l'identifiant utilisateur
function redirectToProfile(userId) {
    const profileUrl = `create_user.html?id=${userId}`;
    window.location.replace(profileUrl);
}
