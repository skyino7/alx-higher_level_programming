$(document).ready(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=f',
    method: 'GET',
    success: function (data) {
      $('div#hello').text(data.hello);
    }
  });
});
