var subnums = new Set()
    
var lectures = document.querySelectorAll('.color')
for (lecture of lectures) {
    subnum = lecture.getAttribute('value')
    subnums.add(subnum)
}

subnums = Array.from(subnums)

for (lecture of lectures) {
    subnum = lecture.getAttribute('value')
    i = subnums.findIndex((element) => element == subnum)
    lecture.classList.add(`color${i}`)
}




//////////////////////bbModal/////////////////////////////////

// Get the modal
var bbmodal = document.getElementById("bbModal");

// Get the button that opens the modal
var bbbtn = document.getElementById("bbBtn");

// Get the <span> element that closes the modal
var bbspan = document.getElementsByClassName("cancel")[0];

// When the user clicks on the button, open the modal
bbbtn.onclick = function() {
  bbmodal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
bbspan.onclick = function() {
  bbmodal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == mymodal) {
    bbmodal.style.display = "none";
    mymodal.style.display = "none";
  }
}
///////////////////////////////////////////////////////////////

////////////////////////myModal/////////////////////////////
// Get the modal
var mymodal = document.getElementById("myModal");
var mymodal_info = document.querySelector(".myModal-info")
var mymodal_menu1 = document.querySelector(".myModal-menu1")
var mymodal_menu2 = document.querySelector(".myModal-menu2")


// Get the button that opens the modal
var mybtns = document.querySelectorAll(".myBtn");


for (mybtn of mybtns){

  mybtn.onclick = function(){
    mymodal.style.display = "block";
    let subnum = this.getAttribute('value');
    mymodal_menu1.setAttribute('href', `/community/friends/${subnum}`)
    mymodal_menu2.setAttribute('href', `/community/board/${subnum}`)
  }
}


// Get the <span> element that closes the modal
var myspan = document.getElementsByClassName("close")[0];


// When the user clicks on <span> (x), close the modal
myspan.onclick = function() {
  mymodal.style.display = "none";
}




const submit = document.querySelector(".submit");
const loading = document.querySelector(".loading");
const cancel = document.querySelector(".cancel");
const bbid = document.querySelector(".bbid");
const bbpw = document.querySelector(".bbpw");
const status = document.querySelector(".status");
const bbBtn = document.querySelector("#bbBtn");
const plus = document.querySelector(".fa-plus")

bbBtn.addEventListener("mouseover", function(event){
  bbBtn.classList.add("hover");
  plus.classList.add("fa-spin");
  plus.classList.add("fa-fw");
})
bbBtn.addEventListener("mouseout", function(event){
  bbBtn.classList.remove("hover");
  plus.classList.remove("fa-spin");
  plus.classList.remove("fa-fw");
})

submit.addEventListener("click", function(event){
  submit.classList.add("none");
  loading.classList.remove("loading");
  cancel.classList.add("none");
  bbid.classList.add("none");
  bbpw.classList.add("none");
  status.textContent = "블랙보드에서 정보를 가져오는 중입니다";
});