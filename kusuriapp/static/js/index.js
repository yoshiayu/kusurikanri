const searchText = document.getElementById("js-search-text");
const searchBtn = document.getElementById("js-search-btn");
const csrftoken = Cookies.get('csrftoken');
const medicinelistElement = document.getElementById("js-medicine-list");

searchText.addEventListener("input", function () {
    const text = searchText.value;
    postSearchText(text);
}, false);

searchBtn.addEventListener("click", function () {
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

    while (medicinelistElement.firstChild) {
        medicinelistElement.removeChild(medicinelistElement.firstChild);
    }

    for (let medicine of filterdMedicines) {
        console.log("pk", medicine.pk);
        console.log("initials:", medicine.fields.initials);
        console.log("medicine_name:", medicine.fields.medicine_name);
        console.log("company_name:", medicine.fields.company_name);
        createFilteredElement(medicine.pk, medicine.fields.initials, medicine.fields.medicine_name, medicine.fields.company_name);
    }
}

function createFilteredElement(id, initials, medicineName, companyName) {
    async function createFilteredElement(initials, link, medicineName, companyName) {
        const listItemElement = document.createElement("li");
        listItemElement.classList.add("medicine-list-item");
        console.log(listItemElement);

        const linkText = "/static/" + String(id) + "/detail/";
        console.log(linkText);
        const listLinkElement = document.createElement("a");
        listLinkElement.classList.add("link-text");
        listItemElement.setAttribute("href", linkText);
        listItemElement.textContent = title;
        console.log(listLinkElement);

        const listDateElement = document.createElement("div");
        listDateElement.classList.add("medicine-date");
        listDateElement.classList.innerHTML = "作成日:" + medicineName + "<br>更新日:" + companyName;
        console.log(listDateElement);

        listItemElement.appendChild(listLinkElement);
        listItemElement.appendChild(listDateElement);

        medicinelistElement.appendChild(listItemElement);
    }
}