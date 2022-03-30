$(function(){
    $("[name='per_page']").change(function(){
        var $frm = $("[name='frm_per_page']");
        $frm.attr("method", "POST");
        $frm.attr("action", "/board/per_page/");
        $frm.submit();
    });
});