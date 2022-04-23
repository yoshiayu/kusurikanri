//setInterval(() => {
//    fetch("/get-alarm/")
//    .then(response  => response.json())
//    .then(data => push(data));
//},1000);

//function push(data) {
//    push.create('お時間です。',{
//        body:'お薬を飲んでください。'})
//        //console.log(data);
//}

let count = 0;
const countUp = () => {
    console.log(count++);
    const timeoutId = setTimeout(countUp, 1000);
    if(count > 10){
        clearTimeout(timeoutId);
    }
}
countUp();

window.onload = function() {
    Notification.requestPermission();
    setInterval(checkTime, 1000);   
 };
 
 const checkTime = function() {
    let previousMinutes;
    const options = {
        body: "調子はどうですか？",
        //icon: "images/medicine13.webp"
    };
    return function() {
        const currentTime = new Date();
        const minutes = currentTime.getMinutes();
        if (previousMinutes !== minutes && minutes % 15 === 0) {
            previousMinutes = minutes;
            const notification = new Notification("お薬を飲む時間です!", options);
        }
    }  
 }();