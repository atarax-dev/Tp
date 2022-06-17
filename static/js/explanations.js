let resultMessage = document.getElementById("result-message");
try{
    if (resultMessage.textContent == "Ce site répond correctement"){
    resultMessage.style.color = "green";
    }
    else if (resultMessage.textContent == "Ce site ne répond pas ou l'entrée est invalide"){
    resultMessage.style.color = "red";
    }
    } catch (error) {
    console.log(error.message)
    console.log("La variable n'est pas encore créée par le rendu, il faut exécuter la fonction")
    }