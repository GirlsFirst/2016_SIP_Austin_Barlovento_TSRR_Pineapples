function changeColor(){
    var words = document.getElementById("newItem");
    if (words.style.color.match("white")){
       words.style.color = "black";
    }
    else{
      words.style.color = "white";
    }
}
