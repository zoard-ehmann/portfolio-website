$(document).ready(function() {
  checkMsgLength(trackMsgLength());

  $('#message').keyup(function() {
    checkMsgLength(trackMsgLength());
  });

});

function trackMsgLength() {
  var text_length = $('#message').val().length;

  $('#my-progress-bar').html(text_length);
  $('#my-progress-bar').attr('aria-valuenow', text_length).css('width', text_length+'%');

  return text_length;
}

function checkMsgLength(text_length) {
  if(text_length >= 100) {
    $('#my-progress-bar').removeClass('bg-danger');
    $('#my-progress-bar').addClass('bg-success');
  } else {
    $('#my-progress-bar').removeClass('bg-success');
    $('#my-progress-bar').addClass('bg-danger');
  }
}