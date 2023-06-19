
// Dark Mode
var DarkMode = document.getElementById('dark-theme');
DarkMode.onclick = function(){
    document.body.classList.toggle("dark-mode");
    var theme;
    if(document.body.classList.contains("dark-mode")){
      
        theme ="DARK";  
    }
    else{
       
        theme ="LIGHT"
    }

    // save to localStorage
    localStorage.setItem('PageTheme',JSON.stringify(theme));
}

let GetTheme = JSON.parse(localStorage.getItem("PageTheme"));
if(GetTheme ==="DARK"){
    let icon = document.getElementById('icon');
    icon.src="../static/imges/sun.png";
    let iconText = document.getElementById('icontext');
    iconText.innerText ="Light";
    document.body.classList ='dark-mode';
   
}
else{
    let icon = document.getElementById('icon');
    icon.src="../static/imges/moon.png";
    let iconText = document.getElementById('icontext');
    iconText.innerText ="Night";
}


// dark mode js end 



var ErMess = document.getElementById('er_mess');
function seterr(ermess){
    ErMess.innerHTML = ermess;
}

function is_valid(){
   
    var regex =/^(?:https?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))((\w|-){11})(?:\S+)?$/;
    var ytlinkname = document.forms['myform']['yt_link'].value;
    if(ytlinkname.length < 1){
        seterr("<p>this can not be empty</p>");
        return   false;
    }
    else if(regex.test(ytlinkname) == false) {
        seterr("<p>this is not valid youtube link </p>");
        return false;
    }
    
    return true;  
   
}
setInterval(() => {
    ErMess.innerHTML="";
}, 5000);

var Preloader =document.getElementById('loading');
window.addEventListener('load',function(){
    Preloader.style.display="none"
})







