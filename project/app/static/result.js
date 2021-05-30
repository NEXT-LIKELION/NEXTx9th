
html2canvas(document.querySelector("#capture")).then(canvas => {
    document.body.appendChild(canvas)
});

