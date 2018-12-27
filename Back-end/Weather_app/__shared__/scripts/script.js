const plusSign = document.querySelector("#plus-sign");
const extSummary = document.querySelector(".grid4");
var isOpen = true;
// console.log(plusSignLi);
function showText() {
  if (extSummary.style.display === "none") {
    extSummary.style.display = "";
  } else {
    extSummary.style.display = "none";
  }
}
function showAnimate() {
  plusSign.classList.toggle('open-state');
  setTimeout(showText, 550);
  
}
plusSign.addEventListener('click', showAnimate);