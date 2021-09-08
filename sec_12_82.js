$('h1').click(function(){
    $(this).text("I was changed..")
})

$('p').click(function(){
    console.log("Click on paragraph")
})

$('input').eq(0).keypress(function(event){
    if (event.which === 13) {
        $('h1').toggleClass('turnBlue')
    }
})

$('h2').on('dblclick',function(){
    $(this).toggleClass('turnBlue')
})