function mostrarModal(e) {
    console.log("abriu modal")
    console.log(e)
    let id = e.getAttribute('data-id');
    document.querySelector('.showmodal-' + id).style.display = "block";
}

function fecharModal(e) {
    console.log("fechou modal")
    console.log(e)
    let id = e.getAttribute('data-id');
    document.querySelector('.showmodal-' + id).style.display = "none";
}