const submitForm = data => {
    var XHR = new XMLHttpRequest();

    // Define what happens on successful data submission
    XHR.addEventListener("load", function(event) {
        alert(event.target.responseText);
    });

    // Define what happens in case of error
    XHR.addEventListener("error", function(event) {
        alert('Oops! Something went wrong.');
    });

    // Set up our request
    XHR.open("GET", "localhost:5500/?" + data.latitude + "," + data.longitude);

    // The data sent is what the user provided in the form
    XHR.send({});
    
    // Access the form element...
    var form = document.getElementById("myForm");
}