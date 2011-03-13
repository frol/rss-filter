$(function() {
    $('a[rel="link"]').click(function() {
        var link = $(this);
        $.getJSON(link.get(0).href, function(data) {
            text = data.text;
            if (data.status == 'ok')
                text = '<img class="icon_success" src="/site_media/img/success.png"> ' + text;
            else
                text = '<img class="icon_error" src="/site_media/img/error.png"> ' + text;
//            text = '<p class="disabled_action">' + text + '</p>';
            link.parent().get(0).innerHTML = text;
        });
        return false;
    });
});

/*
 * jQuery outerHTML
 *
 * Copyright (c) 2008 Ca-Phun Ung <caphun at yelotofu dot com>
 * Dual licensed under the MIT (MIT-LICENSE.txt)
 * and GPL (GPL-LICENSE.txt) licenses.
 *
 * http://yelotofu.com/labs/jquery/snippets/outerhtml/
 *
 * outerHTML is based on the outerHTML work done by Brandon Aaron
 * But adds the ability to replace an element.
 */

(function($) {
	$.fn.outerHTML = function(s) {
		return (s) 
			? this.before(s).remove() 
			: $('<p>').append(this.eq(0).clone()).html();
	}
})(jQuery);
