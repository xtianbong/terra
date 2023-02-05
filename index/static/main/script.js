$(document).ready(function() {
    $('.minus').click(function () {
        var $input = $(this).parent().find('input');
        var count = parseInt($input.val()) - 1;
        count = count < 1 ? 1 : count;
        $input.val(count);
        $input.change();
        return false;
    });
    $('.plus').click(function () {
        var $input = $(this).parent().find('input');
        $input.val(parseInt($input.val()) + 1);
        $input.change();
        return false;
    });
});


//big button scripts

var save = document.querySelector("#save-button");
var load = document.querySelector("#load-button");
var apply = document.querySelector("#apply-button");
var darkness = document.querySelector(".darkness-img")

save.addEventListener("click",saveIt);
load.addEventListener("click",loadIt);
apply.addEventListener("click",applyIt);

var saveBox = document.querySelector("#save-box")
var loadBox = document.querySelector("#load-box")
var applyBox = document.querySelector("#apply-box")




function saveIt(){
    //display box
    saveBox.classList.add("visible-box");
    darkness.classList.add("visible-box");
    

    //send data to stinky django form
    document.querySelector("#id_name").value = document.querySelector("#new-profile").value;
    document.querySelector("#id_max_temp").value = document.querySelector("#max-temp").value;
    document.querySelector("#id_min_temp").value = document.querySelector("#min-temp").value;
    document.querySelector("#id_max_hum").value = document.querySelector("#max-hum").value;
    document.querySelector("#id_min_hum").value = document.querySelector("#min-hum").value;
    document.querySelector("#id_fan_int").value = document.querySelector("#fan-int").value;
    document.querySelector("#id_fan_dur").value = document.querySelector("#fan-dur").value;

    
    document.querySelector("#final-save").addEventListener("click",()=>{
        saveBox.classList.remove("visible-box");
        darkness.classList.remove("visible-box");
        document.querySelector("#new-submit").click();
    });
}

function loadIt(){
    loadBox.classList.add("visible-box")
    darkness.classList.add("visible-box");

    finalLoad = document.querySelector("#final-load")
    finalLoad.addEventListener("click",()=>{
        loadBox.classList.remove("visible-box");
        darkness.classList.remove("visible-box");

        //load data from selected profile
        var selected = document.querySelector(".selected");
        var records = document.querySelectorAll(".record");
        //console.log(selected);
        records.forEach(r=>{
            //console.log(r);
            if(r.id.substring(0,selected.id.length)==selected.id){
                var selectedRecord=r;
                //console.log(r.firstChild.text);
                //console.log(selected.text);
                console.log(r.id.substring(0,selected.id.length));
                console.log(r.children);
                document.querySelector("#max-temp").value=r.children[1].textContent;
                document.querySelector("#min-temp").value=r.children[2].textContent;
                document.querySelector("#max-hum").value=r.children[3].textContent;
                document.querySelector("#min-hum").value=r.children[4].textContent;
                document.querySelector("#fan-int").value=r.children[5].textContent;
                document.querySelector("#fan-dur").value=r.children[6].textContent;
            }
        });
    })
}

//add class to profile selected for load
profiles = document.querySelectorAll(".profile");
profiles.forEach(p=>{
    p.addEventListener("click",()=>{
        //unselect all profiles when any profile is selected
        profiles.forEach(pp=>{
            pp.classList.remove("selected")
        })
        p.classList.add("selected")
    })
});
function applyIt(){
    //apply.classList.add("greyed");
    var applied = document.querySelector("#id_applied").value;
    applied = true;
}

//close overlays when you click outside them
darkness.addEventListener("click",closeOverlay);
function closeOverlay(){
    saveBox.classList.remove("visible-box");
    loadBox.classList.remove("visible-box");
    applyBox.classList.remove("visible-box");
    darkness.classList.remove("visible-box")
}

var oldForm = document.querySelector("#old-form");
var newForm = document.querySelector("#new-form");

function applyGrey(){
    //checks if the current values correspond to the inputted values. if so apply is greyed out
    //this implementation seemed simpler that a for loop, so I went with this
    /*
    var a = document.querySelector("#id_name").value == document.querySelector("#new-profile").value;
    var b = document.querySelector("#id_max_temp").value == document.querySelector("#max-temp").value;
    var c = document.querySelector("#id_min_temp").value == document.querySelector("#min-temp").value;
    var d = document.querySelector("#id_max_hum").value == document.querySelector("#max-hum").value;
    var e = document.querySelector("#id_min_hum").value == document.querySelector("#min-hum").value;
    var f = document.querySelector("#id_fan_int").value == document.querySelector("#fan-int").value;
    var g = document.querySelector("#id_fan_dur").value == document.querySelector("#fan-dur").value;

    if(a&&b&&c&&d&&e&&f&&g){
        apply.classList.add("greyed");
    }
    else{
        apply.classList.remove("greyed");
    }
    */
    applied = true;
    //make sure a name is entered in savebox
    if(document.querySelector("#new-profile").value==""){document.querySelector("#final-save").classList.add("greyed")}
    else{document.querySelector("#final-save").classList.remove("greyed")};
}

//run applyGrey every tenth of a secong
window.setInterval(applyGrey,100)