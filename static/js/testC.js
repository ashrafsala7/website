$(function() {
    $("a.link").on("click", function(){
      $(this).addClass('circle');
      $(".testC").addClass('move');
    });
});
