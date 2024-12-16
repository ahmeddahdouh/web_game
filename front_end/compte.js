const urlParams = new URLSearchParams(window.location.search);
const compteId = urlParams.get('id');

const SERVER_URL = "http://127.0.0.1:8090";

async function getCompteById() {
    try {
        const response = await fetch(`${SERVER_URL}/compte/${compteId}`);

        if (!response.ok) {
            throw new Error(`Erreur HTTP! Statut: ${response.status}`);
        }
        const data = await response.json();
        updateProfileInfo(data);

    } catch (error) {
        console.error("Erreur lors de la récupération du compte :", error);
    }
}

function updateProfileInfo(data) {
    document.getElementById('nom').textContent = `Bienvenue : ${data.nom} ${data.prenom}`;
    document.ge

    tElementById('adr').textContent = `Adresse : ${data.addresse}`;
    document.getElementById('niveau').textContent = `Niveau : ${data.niveau}`;
    document.getElementById('score').textContent = `Score : ${data.score}`;

    const avatar = document.getElementById("profile-photo");
    avatar.src = `${SERVER_URL}${data.avatar}`;
    console.log(`Source de l'avatar : ${avatar.src}`);
}

// Gestion du bouton de déconnexion
function setupLogoutButton() {
    const buttonLogOut = document.getElementById("deconnexion");

    if (!buttonLogOut) {
        console.error("Bouton de déconnexion introuvable dans le DOM.");
        return;
    }

    buttonLogOut.addEventListener("click", () => {
        window.location.href = 'login.html';
    });
}

// Initialisation de la page
function initialize() {
    setupLogoutButton();
    getCompteById();
}

// Lancer l'initialisation après le chargement de la page
document.addEventListener("DOMContentLoaded", initialize);
