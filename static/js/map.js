var data;

var setView_x = 0,
    setView_y = 0;


window.addEventListener("load", async(event) => {
    const response = await fetch('/api/projects');
    data = await response.json();
    // console.log(data)

    total_coord = 0;

    // console.log(data.length);

    for (i = 0; i < data.length; i++) {
        console.log(data[i].location_coordinates.length);

        for (j = 0; j < data[i].location_coordinates.length; j++) {
            // console.log();
            // console.log(i + " " + data[i].location_coordinates[j]);
            // project_name
            L.marker([data[i].location_coordinates[j][0], data[i].location_coordinates[j][1]])
                .bindPopup(data[i].project_name)
                .addTo(map)
                .on('mouseover', onClick);

            setView_x += data[i].location_coordinates[j][0];
            setView_y += data[i].location_coordinates[j][1];
            total_coord++;
        }

        // console.log(data[i].location_coordinates);
        // console.log(data[i].location_coordinates.length);
    }

    setView_x = setView_x / total_coord;
    setView_y = setView_y / total_coord;

    console.log("setx -- " + setView_x);
    console.log("sety -- " + setView_y)

});

// var map = L.map('map').setView([23.72791662761905, 90.40686054500544], 13);


var map = L.map('map').setView([23.7461081171818, 90.40092292250247], 13);


L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// const response = await fetch('/api/projects');
// var data = await response.json();
// console.log(data)

// L.marker([51.5, -0.09]).addTo(map)
//     .on('mouseover', onClick);

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