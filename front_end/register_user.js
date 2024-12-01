const urlParams = new URLSearchParams(window.location.search);
const compte_id = urlParams.get('id');

document.getElementById("register-form").addEventListener("submit",
    async (event) => {
        event.preventDefault();
        const user_login = document.getElementById("user_login").value;
        const password = document.getElementById("password").value;
        const now = new Date().toISOString();

        // Construire l'objet JSON
        const data = {
            user_login,
            password,
            user_created_at: now,
            user_login_date: now,
            user_role: "test",
            compte_id,
        };

        try {
            const response = await fetch("http://127.0.0.1:8090/users/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
            });

            if (response.ok) {
                const responseData = await response.json();
                Swal.fire({
                        title: `Bravo ${responseData.user_login}!`,
                        text: 'Your operation was completed.',
                        icon: 'success',
                        confirmButtonText: 'OK',
                        confirmButton : true
                    }).then((result)=>{
                        if (result.isConfirmed){
                              window.location.replace(`compte.html?id=${compte_id}`);

                        }});

            } else {
                const errorText = await response.text();
                console.error("Erreur lors de l'inscription :", errorText);
                alert("L'inscription a échoué. Veuillez réessayer.");
            }
        } catch (error) {
            console.error("Erreur réseau ou serveur :", error);
            alert("Impossible de se connecter au serveur.");
        }
    });
