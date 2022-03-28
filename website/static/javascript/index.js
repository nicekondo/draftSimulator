function myFunction() {
    let np= document.getElementById("numberOfPlayers").value;
    let no= document.getElementById("numberOfObjects").value;
    document.getElementById("demo").innerHTML = "球団数は"+np+"です";
    document.getElementById("demo2").innerHTML = "選手の総数は"+no+"です";
    console.log("起動テスト");
}