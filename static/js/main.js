const locBtn = document.getElementById("find-loc");

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        console.log("Geolocation is not supported by this browser.");
    }
}

function showPosition(position) {
    console.log(position.coords);
}

locBtn.addEventListener("click", getLocation);