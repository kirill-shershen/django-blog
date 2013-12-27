(function($){
    $(document).ready(function() {
        var pub = $('#id_public')[0];
        var tags = $('#id_tags')[0];
        tags.readOnly = !pub.checked;
        addEvent(pub, 'click', function() {
            if (!pub.checked){
                tags.value = '';
                tags.readOnly = true;
            } else {
                tags.readOnly = false;
            }
        });
    });
})(grp.jQuery);