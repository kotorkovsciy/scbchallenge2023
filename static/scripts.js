function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function setCookie(name, value) {
    document.cookie = name + "=" + value + ";SameSite=Lax;";
}

var checkboxes = document.querySelectorAll('input[type="checkbox"]');

function moveActiveCheckboxToTop(checkbox) {
    checkbox.parentNode.prepend(checkbox);
}

checkboxes.forEach(function (checkbox) {
    var savedValue = getCookie(checkbox.name + "_" + checkbox.value);

    if (savedValue) {
        checkbox.checked = true;
    }

    checkbox.addEventListener('change', function () {
        var params = new URLSearchParams(window.location.search);

        if (checkbox.checked) {
            params.append(checkbox.name, checkbox.value);
            setCookie(checkbox.name + "_" + checkbox.value, checkbox.name + "_" + checkbox.value);
        } else {
            params.delete(checkbox.name);
            setCookie(checkbox.name + "_" + checkbox.value, '');
        }
        var newUrl = `${window.location.pathname}?${params.toString()}`;

        window.location.href = newUrl;
    });
});