document.querySelector("label[for='id_vacancy']").style.visibility = "hidden"
document.querySelector("label[for='id_created_by']").style.visibility = "hidden"


async function get_resumes_user(id){
    let data = {
        "id": id
    };

    let response = await fetch(fullUrl + `/get_resumes_user/`, {
        method: "POST",
        headers: {
            'X-CSRFToken': csrftoken,
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data),
    });

    response = await response.json();
    return response.resumes;
}

async function update_resumes(id){
    var resumes = document.getElementById("id_resume");
    resumes.innerHTML = "";
    let response = await get_resumes_user(id);

    for (let i = 0; i < response.length; i++) {
        let option = document.createElement("option");
        option.text = response[i].title;
        option.value = response[i].id;
        resumes.add(option);
    }
}
