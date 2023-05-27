document.getElementById("id_city").disabled = true;

async function get_city() {
    var region = document.getElementById("id_region");
    var city = document.getElementById("id_city");

    if (region.value.trim() !== '') {
        city.disabled = false;
        let cities_list = await cities(region.value);
        city.innerHTML = "";
        if (cities_list.length != 0) {
            for (let i = 0; i < cities_list.length; i++) {
                let option = document.createElement("option");
                option.value = cities_list[i][0];
                option.innerHTML = cities_list[i][1];
                city.appendChild(option);
            }
        }
        else {
            city.disabled = true;
            let option = document.createElement("option");
            option.value = region.value;
            option.innerHTML = await get_area(region.value);
            city.appendChild(option);
        }
    } else {
        city.disabled = true;
    }
}

async function cities(id){
    let data = {
        "id": id
    };

    let response = await fetch(fullUrl + `/get_cities/`, {
        method: "POST",
        headers: {
            'X-CSRFToken': csrftoken,
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data),
    });

    response = await response.json();
    return response.cities
}

async function get_area(id){
    let data = {
        "id": id
    };

    let response = await fetch(fullUrl + `/get_area/`, {
        method: "POST",
        headers: {
            'X-CSRFToken': csrftoken,
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data),
    });

    response = await response.json();
    return response.area.name
}
