// Constantes Globales
const BASE_URL = "http://127.0.0.1:8090";
const urlParams = new URLSearchParams(window.location.search);
const compteId = urlParams.get('id_compte');

// Fonction pour gérer les erreurs HTTP
function handleHttpErrors(response) {
    if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
}

// Fonction principale pour initialiser l'application
async function initApp() {
    try {
        const objects = await fetchObjects();
        populateDropdown(objects);
        getInventaire();
    } catch (error) {
        console.error("Erreur lors de l'initialisation de l'application :", error);
    }
}

// Récupérer les objets depuis l'API
async function fetchObjects() {
    const response = await fetch(`${BASE_URL}/object/`);
    return handleHttpErrors(response);
}

// Remplir le menu déroulant avec des objets
function populateDropdown(items) {
    const dropdown = document.getElementById("dropdown");
    const quantityInput = document.getElementById("quantity");

    if (!dropdown || !quantityInput) {
        console.error("Dropdown ou champ quantité introuvable dans le DOM.");
        return;
    }

    items.forEach(item => {
        const option = document.createElement("option");
        option.value = item.id_objet;
        option.textContent = item.nom_objet;
        dropdown.appendChild(option);
    });

    // Gestion de l'événement de soumission
    const addObjectForm = document.getElementById("addObjectForm");
    if (addObjectForm) {
        addObjectForm.addEventListener("submit", (event) => handleSubmit(event, dropdown, quantityInput));
    }
}

// Gestion de la soumission du formulaire
async function handleSubmit(event, dropdown, quantityInput) {
    event.preventDefault();

    const data = {
        id_compte: parseInt(compteId),
        id_objet: dropdown.value,
        qty: quantityInput.value,
    };

    try {
        const response = await fetch(`${BASE_URL}/inventaire/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data),
        });

        if (response.ok) {
            $('#inventoryModalCenter').modal('hide');
            getInventaire();
        } else if (response.status === 400) {
            const errorData = await response.json();
            const errorMessage = errorData.detail || "Données invalides";
            showAlert("Oups, erreur !", errorMessage, "error");
        }
    } catch (error) {
        console.error("Erreur réseau :", error);
        $('#inventoryModalCenter').modal('hide');
    }
}

// Afficher une alerte personnalisée
function showAlert(title, text, icon) {
    Swal.fire({
        title,
        text,
        icon,
        confirmButton: true,
        confirmButtonText: 'OK',
    });
}

// Récupérer l'inventaire
async function getInventaire() {
    try {
        const response = await fetch(`${BASE_URL}/inventaire/?id_compte=${compteId}`);
        const items = await handleHttpErrors(response);
        populateTable(items);
    } catch (error) {
        console.error("Erreur lors de la récupération de l'inventaire :", error);
    }
}

// Remplir la table avec les données d'inventaire
function populateTable(items) {
    const tableBody = document.querySelector("#table_inventory tbody");

    if (!tableBody) {
        console.error("Table introuvable dans le DOM.");
        return;
    }

    tableBody.innerHTML = "";
    items.forEach(item => {
        const row = document.createElement("tr");

        const nameCell = createCell(item.nom_objet, "center");
        const qtyCell = createCell(item.qty, "center");
        const actionsCell = createActionsCell(item);

        row.append(nameCell, qtyCell, actionsCell);
        tableBody.appendChild(row);
    });
}

// Créer une cellule de tableau
function createCell(content, align = "left") {
    const cell = document.createElement("td");
    cell.textContent = content;
    cell.style.textAlign = align;
    return cell;
}

// Créer une cellule contenant les actions
function createActionsCell(item) {
    const actionsCell = document.createElement("td");
    actionsCell.style.textAlign = "center";

    const editLink = createActionLink("Modifier", () => openEditModal(item));
    const deleteLink = createActionLink("Supprimer", () => handleDelete(item));

    actionsCell.append(editLink, deleteLink);
    return actionsCell;
}

// Créer un lien d'action
function createActionLink(text, onClick) {
    const link = document.createElement("a");
    link.href = "#";
    link.textContent = text;
    link.style.marginRight = "10px";
    link.addEventListener("click", onClick);
    return link;
}

// Ouvrir le modal d'édition
function openEditModal(item) {
    $('#inventoryModalCenter').modal('show');
    const modal = $("#inventoryModalCenter");
    modal.find('.modal-title').text(`Modifier l'élément ${item.nom_objet}`);
    modal.find("#quantity").val(item.qty);
}

// Supprimer un élément
function handleDelete(item) {
    console.log(`Supprimer l'objet : ${item.nom_objet}`);
}

// Initialisation
initApp();
