const BASE_URL = "http://127.0.0.1:8090";
const urlParams = new URLSearchParams(window.location.search);
const compteId = urlParams.get('id_compte');
let numberObject = 0;
let numberInventoryLines = 0
let objects;
let clickCount = 0;

function OnChangeFilter(){
    const sortedDropDown  = document.getElementById("sortedDropDown")
    sortedDropDown.addEventListener("change",(event)=>{
        console.log(event.target.value)
        getInventaire(event.target.value)
    })
}

function hideButtonCondition() {
    if (numberObject == numberInventoryLines) {
        document.getElementById("add-element").style.display = 'none';
    } else
        document.getElementById("add-element").style.display = 'block';
}

function handleHttpErrors(response) {
    if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
}

function OpenCreateModal() {
    const addElementToInventory = document.getElementById("add-element");
    addElementToInventory.addEventListener("click", () => {
        if (numberObject != numberInventoryLines) {
            openModal(undefined, "create");
        } else {
            showAlert("erreur",
                "Vous n'avez pas le droit d'ajouter une ligne, tous les objets sont déjà disponibles.",
                "danger");
        }
    });

}


async function initApp() {

    try {
        getInventaire();

    } catch (error) {
        console.error("Erreur lors de l'initialisation de l'application :", error);
    }
    OpenCreateModal();
    OnChangeFilter();
}

async function fetchObjects() {
    const response = await fetch(`${BASE_URL}/object/`);
    return handleHttpErrors(response);
}


function populateDropdown(items) {
    const dropdown = document.getElementById("dropdown");


    dropdown.innerHTML = ""
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


    const addObjectForm = document.getElementById("addObjectForm");
    if (addObjectForm) {
        clickCount = 0
        addObjectForm.addEventListener("submit", (event) => {
            event.preventDefault(); // Empêche l'envoi pour débogage (à retirer si nécessaire)
            clickCount++;
            if (clickCount < 2) {
                handleSubmit(event, dropdown, quantityInput);
            }

        });
    }

}


// Gestion de la soumission du formulaire
async function handleSubmit(event, dropdown, quantityInput) {
   debugger;
    event.preventDefault();
    debugger;
    let data = {
        id_compte: parseInt(compteId),
        id_objet: dropdown.value,
        qty: quantityInput.value,
    };
    if (event.submitter.value != "Modifier") {
        try {
            const response = await fetch(`${BASE_URL}/inventaire/`, {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify(data),
            });

            if (response.ok) {
                $('#inventoryModalCenter').modal('hide');
                showAlert("Bravo !", "Element ajouter avec succées", "success")
                getInventaire();

            } else if (response.status === 400) {
                const errorData = await response.json();
                const errorMessage = errorData.detail || "Données invalides";
                showAlert("Oups, erreur !", errorMessage, "error");
            }
        } catch (error) {
            consol.error("Erreur réseau :", error);
            $('#inventoryModalCenter').modal('hide');
        }


    } else {
        try {
            const response = await fetch(`${BASE_URL}/inventaire/`, {
                method: "PUT",
                headers: {"Content-Type": "application/json"},
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
async function getInventaire(target = undefined) {

    try {
        objects = await fetchObjects();
        numberObject = objects.length
        const response = await fetch(`${BASE_URL}/inventaire/?id_compte=${compteId}`);
        const items = await handleHttpErrors(response);
        numberInventoryLines = items.length
        hideButtonCondition()
        inventaireObjects = items.map(item => item.id_objet);
        const sortedDataByObject = [...items].sort((a, b) => a.nom_objet.localeCompare(b.nom_objet));
        const sortedDataByQty = [...items].sort((a, b) => a.qty - b.qty);
        debugger;
        if (parseInt(target) == 1){
             populateTable(sortedDataByObject);
        }
        else if (parseInt(target)){
            populateTable(sortedDataByQty);
        }else
        {
            populateTable(items)
        }


        objectsToPopulate = objects.filter(item => !inventaireObjects.includes(item.id_objet));
        populateDropdown(objectsToPopulate)
    } catch (error) {
        console.error("Erreur lors de la récupération de l'inventaire :", error);
    }
    hideButtonCondition()
}

function populateTable(items) {
    const tableBody = document.querySelector("#table_inventory tbody");

    if (!tableBody) {
        console.error("Table introuvable dans le DOM.");
        return;
    }

    tableBody.innerHTML = "";

    const sortDropdown = document.getElementById("sortedDropDown")
    const hrElements = document.querySelectorAll('th')
    sortDropdown.innerHTML=""
    hrElements.forEach((hr,index) => {
        option = document.createElement('option')
        option.value = index + 1
        option.text = hr.textContent.trim();
        sortDropdown.appendChild(option)
        hr.style.textAlign = "center"
    })
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

    const editLink = createActionLink("Modifier", () => openModal(item, "edit"));
    const deleteLink = createActionLink("Supprimer", () =>
        Swal.fire({
            title: "Are you sure?",
            text: "You won't be able to revert this!",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#3085d6",
            cancelButtonColor: "#d33",
            confirmButtonText: "Yes, delete it!"
        }).then((result) => {
            if (result.isConfirmed) {
                handleDelete(item);
                Swal.fire({
                    title: "Deleted!",
                    text: "Your file has been deleted.",
                    icon: "success"
                });
            }
        }));


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
function openModal(item = undefined, action) {
    debugger;
    $('#inventoryModalCenter').modal('show');
    const modal = $("#inventoryModalCenter");
    if (action = "edit" && item) {
        populateDropdown(objects)
        modal.find('.modal-title').text(`Modifier l'élément ${item.nom_objet}`);
        modal.find("#dropdown").val(item.id_objet)
        modal.find("#quantity").val(item.qty);
        modal.find("#submit").val("Modifier");
        modal.find("#dropdown").prop("disabled", true);

    } else {

        modal.find('.modal-title').text(`Ajouter un element`);
        modal.find("#dropdown").val("")
        modal.find("#quantity").val("");
        modal.find("#submit").val("Ajouter");
        modal.find("#dropdown").prop("disabled", false);

    }

}

async function handleDelete(item) {


    const data = {
        id_compte: parseInt(compteId),
        id_objet: item.id_objet,
        qty: item.qty,
    };
    try {
        const response = await fetch(`${BASE_URL}/inventaire/`, {
            method: "DELETE",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(data),
        });

        if (response.ok) {
            getInventaire()
        } else {
            console.log(response.json())
        }
    } catch (error) {
        console.log("error :", error)
    }

}


// Initialisation
initApp();
