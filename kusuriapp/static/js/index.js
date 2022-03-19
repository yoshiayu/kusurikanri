const searchText = document.getElementById("js-search-text");
const searchBtn = document.getElementById("js-search-btn");
const csrftoken = Cookies.get('csrftoken');

searchText.addEventListener("input", function() {
    const text = searchText.value;
    postSearchText(text);
});

searchBtn.addEventListener("click", function () {
    const text = searchText.value;
    postSearchText(text);
}, false);

async function postSearchText(searchText) {
    const postBody = {
        text: searchText,
    };
    console.log(postBody);
    const postData = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify(postBody)
    };
    const res = await fetch("/medicine-search/", postData)
    const json = await res.json();
    console.log(json);
}