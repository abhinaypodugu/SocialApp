slider = document.querySelector("#slider")

slider.oninput = function () { document.querySelector("#text").style.fontSize = this.value + "px" }

