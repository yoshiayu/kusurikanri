setInterval(() => {
    fetch("/get-alarm/")
      .then(response => response.json())
      .then(data => push(data));
}, 1000);

function push(data) {
    // Push.create('Hello World!');
}