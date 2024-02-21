/*
 * Notes: don't use this file like a resource function because
 *        it is for the test only, you need to put the fonction
 *        in new .js file and make it like a function :D
 *
 * Read Json file content in Javascript
 * the file in https://walidamriou.github.io/data.json content (just fot test):
 *  {"data": {
 *      "id": "123664",
 *      "name": "bingad",
 *      "date": "12.12.12"
 *  }}
 *
 *
 */
function readJsonFile(file, callback) {
  var rawFile = new XMLHttpRequest();
  rawFile.overrideMimeType("application/json");
  rawFile.open("GET", file, true);
  rawFile.onreadystatechange = function () {
    if (rawFile.readyState === 4 && rawFile.status == "200") {
      callback(rawFile.responseText);
    }
  };
  rawFile.send(null);
}

readJsonFile("https://walidamriou.github.io/data.json", function (text) {
  var data = JSON.parse(text);
  console.log(data);
  //alert(data[0].data);
  var elem = document.getElementById("datadisplay");
  elem.innerHTML = data.data["id"]; //we want to read: "id": "123664"
});
