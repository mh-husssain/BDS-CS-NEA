const balance = document.getElementById('balance');
const forms = document.querySelector('#forms');   
const text = document.getElementById('clear')
//----------------------------------------------------*/
balance.addEventListener('click', (event) => {
    

    // Transform from dynamic to static element
    $("#balance").css("pointer-events", "none"); 
    $("#balance button, #balance input").css("pointer-events", "auto");
    // ^^^ Child elements still need to remain dynamic
    $("#clear").fadeTo(1000, 0);

    setTimeout(function() {
        text.style.display = 'none';
    }, 1000);

    setTimeout(function() {
        balance.classList.add("active");
        balance.classList.add('hover');
    }, 1000);

    setTimeout(function() {
        $("#forms").fadeTo(1000, 0.8);
    }, 1700);
    // Items fade into display
});




/*/ This script runs when #Profile element is clicked
box.addEventListener('click', (event) => { 
    box.classList.add('active'); // Toggle Classes
    profile.classList.add('hover');
        
        setTimeout(function() { //Re-apply the clear class
        for(var i=0; i<box.length; i++) { // Apply function to every element
        box[i].classList.add('clear');
        }
    }, 300); //Delay of 300ms

    setTimeout(function() { // Fade of opacity for GUI purposes
        $("#personalisation").fadeTo(1500, 0.7);
    }, 1600);
});
 // - - - - - - - - - - End Function - - - - - - - - - - - /*/