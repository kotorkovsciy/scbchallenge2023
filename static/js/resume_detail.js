async function delete_resume(id){
    let data = {
        "id": id
    };

    let response = await fetch(fullUrl + `/resume_delete/`, {
        method: "POST",
        headers: {
            'X-CSRFToken': csrftoken,
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data),
    });

    if (response.ok){
        var profile = document.getElementById("profile-info");
        var resume = document.getElementById(`${id}`);
        profile.removeChild(resume);
    }
    response = await response.json();
    alert(response.message)
    location.reload()
}
