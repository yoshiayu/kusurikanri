const searchText = document.getElementById("js-search-text");
const searchBtn = document.getElementById("js-search-btn");
const csrftoken = Cookies.get('csrftoken');
const medicinelistElement = document.getElementById("js-medicine-list");


searchText.addEventListener("input", () => {
    const text = searchText.value;
    postSearchText(text);
}, false);

searchBtn.addEventListener("click", () => {
    const text = searchText.value;
    postSearchText(text);
}, false);

async function postSearchText(searchText) {
    const postBody = {
        text: searchText,
    };
    const postData = {
        method: "POST",
        headers: {
            // "Content-Type": "application/x-www-form-urlencoded",
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify(postBody)
    };
    console.log(postData);
    let res = await fetch("/medicine-search/", postData)
    console.log(res.statusText, res.url);

    const json = await res.json();
    //console.log(json);
    const filterdMedicines = await JSON.parse(json);
    //console.log(filterdMedicines);

    //while (medicinelistElement.firstChild) {
    //    medicinelistElement.removeChild(medicinelistElement.firstChild);
    //}

    const resultsContainer = document.getElementById('autocomplete-results-container');
    while (resultsContainer.firstChild) {
        resultsContainer.removeChild(resultsContainer.lastChild);
    }

    for (let medicine of filterdMedicines) {
        //console.log("pk", medicine.pk);
        //console.log("initials:", medicine.fields.initials);
        //console.log("medicine_name:", medicine.fields.medicine_name);
        //console.log("company_name:", medicine.fields.company_name);
        createFilteredElement(medicine.pk, medicine.fields.initials, medicine.fields.medicine_name, medicine.fields.company_name);
    }
}

function createFilteredElement(id, initials, medicineName, companyName) {
    const listItemElement = document.createElement("div");
    listItemElement.classList.add("s-suggestion");
    listItemElement.textContent = medicineName;
    listItemElement.addEventListener('click', () => {
        document.getElementById('js-search-text').value = medicineName;
        //const element = document.getElementById('autocomplete-results-container');
        //element.remove();
        const resultsContainer = document.getElementById('autocomplete-results-container');
        while (resultsContainer.firstChild) {
            resultsContainer.removeChild(resultsContainer.lastChild);
        }

        //document.getElementById("medicineSelect").value = medicineName;
        //console.log(medicineName);
    });
    listItemElement.addEventListener('click', () => {
        const medicineSelect = document.getElementById('medicine-select');
        const option = document.createElement('option');
        option.textContent = medicineName;
        option.selected = true;
        medicineSelect.appendChild(option);
    });

    //document.getElementById('js-medicine-list');
    //articleListElement.appendChild(listItemElement);
    const resultsContainer = document.getElementById('autocomplete-results-container');
    resultsContainer.appendChild(listItemElement);
    //medicinelistElement.appendChild(listItemElement);






    //const linkText = "/static/" + String(id) + "/detail/";
    //console.log(linkText);
    //const listLinkElement = document.createElement("a");
    //listLinkElement.classList.add("link-text");
    //listLinkElement.setAttribute("href", linkText);
    //listLinkElement.textContent = initials;
    //console.log(listLinkElement);

    //const listDateElement = document.createElement("div");
    //listDateElement.classList.add("js-medicine-list");
    //listDateElement.innerHTML = "薬名:" + medicineName + "<br>会社名:" + companyName;
    //medicinelistItemElement.appendChild(listDateElement);

    //listDateElement.classList.add("medicine-date");
    //listDateElement.innerHTML = "薬名:" + medicineName + "<br>会社名:" + companyName;
    //console.log(listDateElement);

    //listItemElement.appendChild(listLinkElement);
    //listItemElement.appendChild(listDateElement);

    //medicineListElement.appendChild(listItemElement);
}
