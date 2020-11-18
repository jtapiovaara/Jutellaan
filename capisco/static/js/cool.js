$(document).ready(function (){
    $('.radiolist_f').click(function (){
        $.ajax({
            url: 'vaihdafkieli',
            type: 'get',
            data: {
                fkieli_val: $(this).text()
            },
            success: function (response) {
                $('.fkieliotsikko').text(response.fkieliotsikko)
            }
        })
    })
})

$(document).ready(function (){
    $('.radiolist_t').click(function (){
        $.ajax({
            url: 'vaihdatkieli',
            type: 'get',
            data: {
                tkieli_val: $(this).text()
            },
            success: function (response) {
                $('.tkieliotsikko').text(response.tkieliotsikko)
            }
        })
    })
})