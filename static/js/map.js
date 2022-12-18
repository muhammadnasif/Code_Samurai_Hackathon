
var data
window.addEventListener("load", async (event) => {
    const response = await fetch('/api/projects');
    data = await response.json();
    console.log(data)
});

var map = L.map('map').setView([51.505, -0.09], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// const response = await fetch('/api/projects');
// var data = await response.json();
// console.log(data)

L.marker([51.5, -0.09]).addTo(map)
    .on('mouseover', onClick);

async function onClick(e) {
    // const response = await fetch('/api/projects');
    // var data = await response.json();
    // console.log(data[0])
    // var form = document.createElement('form');
    // form.style.visibility = 'hidden'; // no user interaction is necessary
    // form.method = 'POST'; // forms by default use GET query strings
    // form.action = 'project';
    // var input = document.createElement('input');
    // input.name = "affiliated_agency";
    // input.value = data[0].affiliated_agency;
    // form.appendChild(input); // add key/value pair to form
    // document.body.appendChild(form); // forms cannot be submitted outside of body
    // form.submit(); // send the payload and navigate
}
