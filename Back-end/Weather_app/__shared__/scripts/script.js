function celToFer(val1) {
  let res1 = (val1 * 1.8) + 32;
  return Math.floor(res1);
}
function ferToCel(val2) {
  let res2 = (val2 - 32)/1.8;
  return Math.round(res2);
}
function mphToKph(val3){
  let res3 = val3 *  1.609344;
  res3 = parseFloat(res3.toFixed(2));
  return Math.round(res3);
}
function kphToMph(val4){
  let res4 = val4 /  1.609344;
  res4 = parseFloat(res4.toFixed(2));
  return Math.round(res4);
}
// ******************************************************
// SWITCH
$('.toggle').click(function(e) {
  var toggle = this;
  
  e.preventDefault();
  
  $(toggle).toggleClass('toggle--on')
         .toggleClass('toggle--off')
         .addClass('toggle--moving');
  
  setTimeout(function() {
    $(toggle).removeClass('toggle--moving');
  }, 50);
});
$('.toggle2').click(function(e) {
  var toggle2 = this;
  
  e.preventDefault();
  
  $(toggle2).toggleClass('toggle--on2')
         .toggleClass('toggle--off2')
         .addClass('toggle--moving2');
  
  setTimeout(function() {
    $(toggle2).removeClass('toggle--moving2');
  }, 50);
});
// ******************************************************
// SHOW HIDE TEXT WITH PLUS
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
// ******************************************************
// CONTROLE DEGREES
var list = document.getElementsByClassName("degree");
// console.log(list);
const toggle = document.querySelector('.toggle');
// console.log(deg);

function controlDeg() {
  if (toggle.classList.contains('toggle--on')
  ) {
    for (let i = 0; i < list.length; i++) {
      list[i].innerHTML = "°C";      
    }
  }else{
    for (let i = 0; i < list.length; i++) {
      list[i].innerHTML = "°F";
    }
  } 
}

toggle.addEventListener('click', controlDeg);

// ******************************************************
// CONTROLE SPEED UNIT

var listTwo = document.getElementsByClassName("speed");
// console.log(listTwo);
const toggle2 = document.querySelector('.toggle2');
// console.log(toggle2);

function controlSpeed() {
  if (toggle2.classList.contains('toggle--on2')
  ) {
      listTwo[0].innerHTML = "kph";      
  }else{
      listTwo[0].innerHTML = "mph";
  } 
}

toggle2.addEventListener('click', controlSpeed);

// ******************************************************
// CONVERT C TO F

var listThree = document.getElementsByClassName("temperature");
// console.log(listThree);
// console.log(toggle);

function convert() {
  if (toggle.classList.contains('toggle--on')
  ) {
    for (let index = 0; index < listThree.length; index++) {
      listThree[index].innerHTML = ferToCel(listThree[index].innerHTML);       
    }
  }else{
    for (let index = 0; index < listThree.length; index++) {
      listThree[index].innerHTML = celToFer(listThree[index].innerHTML);
    }
  } 
}

toggle.addEventListener('click', convert);


// ******************************************************
// CONVERT KPH TO MPH

var listFour = document.getElementsByClassName("speedVal");
console.log(listFour);
console.log(toggle2);

function convertTwo() {
  if (toggle2.classList.contains('toggle--on2')
  ) {
      listFour[0].innerHTML = mphToKph(listFour[0].innerHTML);       
  }else{
      listFour[0].innerHTML = kphToMph(listFour[0].innerHTML);
  } 
}

toggle2.addEventListener('click', convertTwo);


