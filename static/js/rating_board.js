$('.DOC_TEXT').keyup(function (e) {
    var content = $(this).val(); $('#counter').html("("+content.length+" / 최대 100자)"); //글자수 카운팅 
if (content.length > 100){ //200자 이상일 때 
    alert("최대 100자까지 입력 가능합니다."); 
    $(this).val(content.substring(0, 100)); //넘어간 글자 자르기 
    $('#counter').html("(100 / 최대 100자)");
    }});

    const drawStar = (target) => {
    document.querySelector(`.star span`).style.width = `${target.value * 10}%`;
    }



function chkDel(){
    var r = confirm("삭제하시겠습니까?")
            if(r){
                document.forms['delete'].submit();
            }
}