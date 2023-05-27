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
        params.set("page", 0);
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

var radioButtons = document.querySelectorAll('input[type="radio"]');

radioButtons.forEach(function (radioButton) {
    var savedValue = getCookie(radioButton.name);

    if (savedValue) {
        if (savedValue === radioButton.value) {
            radioButton.checked = true;
        }
    }

    radioButton.addEventListener('change', function () {
        var params = new URLSearchParams(window.location.search);
        params.set("page", 0);
        params.set(radioButton.name, radioButton.value);

        setCookie(radioButton.name, radioButton.value);

        var newUrl = `${window.location.pathname}?${params.toString()}`;

        window.location.href = newUrl;
    });
});

function sortActiveCheckboxes() {
    var activeCheckboxes = Array.from(document.querySelectorAll('.area')).filter(function (checkbox) {
        var savedValue = getCookie(checkbox.name + "_" + checkbox.value);
        return savedValue && checkbox.checked;
    });

    activeCheckboxes.sort(function (checkboxA, checkboxB) {
        var labelA = checkboxA.parentElement.textContent.trim();
        var labelB = checkboxB.parentElement.textContent.trim();
        return labelA.localeCompare(labelB);
    });

    var parentElement = activeCheckboxes[0].parentElement.parentElement;
    activeCheckboxes.forEach(function (checkbox) {
        parentElement.insertBefore(checkbox.parentElement, parentElement.firstChild);
    });

    var activeCheckboxes = Array.from(document.querySelectorAll('.specialization')).filter(function (checkbox) {
        var savedValue = getCookie(checkbox.name + "_" + checkbox.value);
        return savedValue && checkbox.checked;
    });

    activeCheckboxes.sort(function (checkboxA, checkboxB) {
        var labelA = checkboxA.parentElement.textContent.trim();
        var labelB = checkboxB.parentElement.textContent.trim();
        return labelA.localeCompare(labelB);
    });

    var parentElement = activeCheckboxes[0].parentElement.parentElement;
    activeCheckboxes.forEach(function (checkbox) {
        parentElement.insertBefore(checkbox.parentElement, parentElement.firstChild);
    });
}

function update_url() {
    checkboxes.forEach(function (checkbox) {
        var savedValue = getCookie(checkbox.name + "_" + checkbox.value);

        if (savedValue) {
            checkbox.checked = true;
            if (window.location.search.indexOf("&" + checkbox.name + "=" + checkbox.value) === -1) {
                window.history.replaceState({}, '', `${window.location.href + "&" + checkbox.name + "=" + checkbox.value}`);
            }
        }
    });

    radioButtons.forEach(function (radioButton) {
        var savedValue = getCookie(radioButton.name);

        if (savedValue) {
            if (savedValue === radioButton.value) {
                radioButton.checked = true;
                if (window.location.search.indexOf("&" + radioButton.name + "=" + radioButton.value) === -1) {
                    window.history.replaceState({}, '', `${window.location.href + "&" + radioButton.name + "=" + radioButton.value}`);
                }
            }
        }
    });

    sortActiveCheckboxes();
}
