const searchText = document.getElementById("js-search-text");
const searchBtn = document.getElementById("js-search-btn");
const csrftoken = Cookies.get('csrftoken');

searchBtn.addEventListener("click", function () {
    console.log("hoge");
    const text = searchText.Value;
    postSearchText(item, text);
}, false);

async function postSearchText(searchText) {
    const postBody = {
        text: searchText,
    };
    console.log(postBody);
    const postData = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
            "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify(postBody)
    };
    console.log(postData);
    const res = await fetch("./", postData)
    const json = await res.json();
    console.log(json);
}