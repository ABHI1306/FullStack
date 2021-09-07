var header = document.querySelector("h1")

header.style.color = 'red'

function getRandomColor(){
    var letter = "0123456789ABCDEF";
    var color = "#";
    for (var i = 0; i < 6; i++) {
        color += letter[Math.floor(Math.random()*16)];
    }
    return color
}

function changeHeader(){
    colorInput = getRandomColor()
    header.style.color = colorInput;
}

setInterval("changeHeader()",500);
