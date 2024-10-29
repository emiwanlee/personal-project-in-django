var myVar = setInterval(myTimer, 100);

function myTimer() {
var d = new Date();
document.getElementById("demo1").innerHTML = "Server Time: " + d.toUTCString();
}