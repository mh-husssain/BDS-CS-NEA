const profile = document.querySelector('#Profile');
const box = document.querySelectorAll('.box');
const personalisation = document.querySelector('#personalisation');   
const pfp = document.querySelector('#file')
const submit = document.querySelector('#save')
var image = "";

/*
pfp.addEventListener("change", function(){
    const reader = new FileReader();
    reader.addEventListener("load", () => {
        image = reader.result;
        document.querySelector('#display').style.backgroundImage = 'url(${image})';
    })
    reader.readAsDataURL(this.files[0])
})*/

for(var i=0; i<box.length; i++) { // Removes the classes for now
    box[i].classList.remove('clear');
}

// Input file when button is clicked
$('#upload').on('click', function(event) {
    event.preventDefault();
    $('#file').trigger('click');
});

 
// This script runs when #Profile element is clicked
profile.addEventListener('click', (event) => { 
    profile.classList.add('active'); // Toggle Classes
    profile.classList.add('hover');

    // Transform from dynamic to static element
    $("#Profile").css("pointer-events", "none"); 
    $("#Profile button, #Profile input").css("pointer-events", "auto");
    // ^^^ Child elements still need to remain dynamic

    setTimeout(function() { //Re-apply the clear class
        for(var i=0; i<box.length; i++) { // Apply function to every element
        box[i].classList.add('clear');
        }
    }, 300); //Delay of 300ms

    setTimeout(function() { // Fade of opacity for GUI purposes
        $("#personalisation").fadeTo(1500, 0.7);
    }, 1600);
}); // - - - - - - - - - - End Function - - - - - - - - - - - //


/* This script runs when form is submitted
submit.addEventListener("click", (event) => {
    setTimeout(function() {
        window.location.reload()
    }, 1000); //Delay of 300ms
});





/*
function uploadFile() {
  var file = pfp.files[0];
  var formData = new FormData();
  formData.append('file', file);

  var xhr = new XMLHttpRequest();
  xhr.open('POST', 'menu.html', true);
  xhr.onload = function () {
    if (xhr.status === 200) {
      var result = document.getElementById('result');
      console.log('Success');
      //result.innerHTML = 'File uploaded successfully.';
    } else {
      alert('An error occurred!');
    }
  };
  xhr.send(formData);
}



/*
profile.addEventListener("click", Personalisation);

        personalisation.classList.toggle('hidden');  
        personalisation.classList.toggle('personalisation');    

function Personalisation(){
    box.style.display = 'none';
    var buttons = document.getElementById("Profile");
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].classList.toggle("active");
    }

};


/*$( ".boxProfile" ).click(function() {
    $( ".boxProfile" ).css('background', 'green');
  });

function makeActive(btn) {
    // Remove the "active" class from all buttons
    var buttons = document.getElementsByTagName("div");
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].classList.remove("active");
    }

    // Add the "active" class to the clicked button
    btn.classList.add("");
}
function UserPersonalisation() {
    var buttons = document.getElementsByClassName("boxProfile");
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].classList.toggle("active");
    }
}
*/