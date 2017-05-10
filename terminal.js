
function flash() {
    var text = document.getElementById('dash');
    text.style.color = (text.style.color=='black') ? '#00ff00':'black';
}
var clr = setInterval(flash, 600);