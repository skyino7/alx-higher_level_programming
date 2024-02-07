$(document).ready(function () {
    $('input#btn_translate').click(function () {
        const lang = $('input#language_code').val();
        $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${lang}`, function (data) {
            $('div#hello').text(data.hello);
        });
    });
});
