const btn1 = document.getElementById("btn1")

btn1.addEventListener("mousedown", function(){
    btn1.style.boxShadow = "16px 6px 10px brown";
})

btn1.addEventListener("mouseup", function(){
    btn1.style.boxShadow = "";
})