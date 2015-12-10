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

function speed_up() {
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "?cmd=up", true);
  xhttp.send();
}

function speed_down() {
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "?cmd=down", true);
  xhttp.send();
}

function record() {
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "?cmd=record", true);
  xhttp.send();
}

function stop_record() {
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "?cmd=stop-record", true);
  xhttp.send();
}

function clear() {
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "?cmd=clear", true);
  xhttp.send();
}
