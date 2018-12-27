$('.toggle').click(function(e) {
  var toggle = this;
  
  e.preventDefault();
  
  $(toggle).toggleClass('toggle--on')
         .toggleClass('toggle--off')
         .addClass('toggle--moving');
  
  setTimeout(function() {
    $(toggle).removeClass('toggle--moving');
  }, 200);
});
$('.toggle2').click(function(e) {
  var toggle2 = this;
  
  e.preventDefault();
  
  $(toggle2).toggleClass('toggle--on2')
         .toggleClass('toggle--off2')
         .addClass('toggle--moving2');
  
  setTimeout(function() {
    $(toggle2).removeClass('toggle--moving2');
  }, 200);
});