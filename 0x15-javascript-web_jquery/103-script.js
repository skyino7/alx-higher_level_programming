$(document).ready(function () {

    function fetchTranslation () {
        let langCode = $('#language_code').val();
        const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`;
        $.get(url, function (data) {
            $('div#hello').text(data.hello);
        });
    }

    $('#btn_translate').click(fetchTranslation);

    $('#language_code').keypress(function (e) {
        if (e.which === 13) {
            fetchTranslation();
        }
    });

});
