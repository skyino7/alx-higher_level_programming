$(document).ready(function () {
    $('input#btn_translate').click(function () {
        const lang = $('input#language_code').val();
        $.get(`https://fourtonfish.com/hellosalut/?lang=${lang}`, function (data) {
            $('div#hello').text(data.hello);
        });
    });
});
