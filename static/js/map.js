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

        for (j = 0; j < data[i].location_coordinates.length; j++) {


            L.marker([data[i].location_coordinates[j].coord[0], data[i].location_coordinates[j].coord[1]])
                .bindPopup(data[i].project_name)
                .addTo(map)
                // .on('mouseover', pop_up_modal);
                .addEventListener('click', async() => {
                    console.log("success my boy");

                    console.log(data[i]);

                })
            setView_x += data[i].location_coordinates[j].coord[0];
            setView_y += data[i].location_coordinates[j].coord[1];
            total_coord++;
        }
    }

    setView_x = setView_x / total_coord;
    setView_y = setView_y / total_coord;
    console.log(total_coord);
    console.log(setView_x);
    console.log(setView_y);
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

void function pop_up_modal(e) {
    console.log("button presed")
    console.log(e);


    // document.getElementById('pop-up-project-name').innerText =
    // document.getElementById('pop-up-category').innerText
    // document.getElementById('pop-up-affiliated-agency').innerText
    // document.getElementById('pop-up-description').innerText
    // document.getElementById('pop-up-start-time').innerText
    // document.getElementById('pop-up-completion-time').innerText
    // document.getElementById('pop-up-coord').innerText


}


//leaflet-marker-icon leaflet-zoom-animated leaflet-interactive

$('.leaflet-marker-icon').click(function () {

    console.log("marker button pressed ... ")
})