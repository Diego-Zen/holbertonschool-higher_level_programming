$('DIV#toggle_header').click(function () {
  if ($('HEADER').hasClass('red')) {
    $('HEADER').addClass('green').removeClass('red').css('color', '#FF0000');
  } else {
    $('HEADER').addClass('red').removeClass('green');
  }
});
