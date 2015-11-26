function led() {
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "?cmd=led", true);
  xhttp.send();
}

function fwd() {
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "?cmd=fwd", true);
  xhttp.send();
}

function left() {
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "?cmd=left", true);
  xhttp.send();
}

function stop() {
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "?cmd=stop", true);
  xhttp.send();
}

function right() {
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "?cmd=right", true);
  xhttp.send();
}

function bwd() {
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "?cmd=bwd", true);
  xhttp.send();
}
