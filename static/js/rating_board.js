    $('.DOC_TEXT').keyup(function (e) {
        var content = $(this).val(); $('#counter').html("("+content.length+" / 최대 200자)"); //글자수 카운팅 
    if (content.length > 200){ //200자 이상일 때 
        alert("최대 200자까지 입력 가능합니다."); 
        $(this).val(content.substring(0, 200)); //넘어간 글자 자르기 
        $('#counter').html("(200 / 최대 200자)");
     }});

     const drawStar = (target) => {
        document.querySelector(`.star span`).style.width = `${target.value * 10}%`;
      }