const getCurrentTime = () => {
    const date = new Date();
    yy = (date.getFullYear()) + '년 ',
    mm = date.getMonth() + 1
    mm = (mm <10?'0':'') + mm +'월 ',   
    dd= (date.getDate()<10?'0':'') + date.getDate() +'일 ',
    h = (date.getHours()<10?'0':'') + date.getHours() +': ',
    m = (date.getMinutes()<10?'0':'') + date.getMinutes() + ' '

    console.log(date);

document.querySelector('.nav-bar-nowtime').innerHTML = '🕓' + h + m;
document.querySelector('.class_list-today').innerHTML = '📚' + mm + dd;
};

const initClock = () => {
getCurrentTime();
setInterval(getCurrentTime, 1000);
};

initClock();