$(".btn-next1").click(function (event) {
    if (user_exists) {
        return 1;
    }
        s.valid();
        if ((!user_exists) && s.element("#username") && s.element("#first_name") && s.element("#last_name") && s.element("#bday")) {
            next($(this));
        };

});
$(".btn-next2").click(function () {
    s.valid();
    if (s.element("#country") & s.element("#phone") & s.element("#adress") & s.element("#postal_code")) {
        next($(this));
    };
});

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function next(button) {
    if (user_exists) { return 0 };
    var parent_fieldset = button.parents('fieldset');
    var next_step = true;

    parent_fieldset.find('input[type="text"], input[type="password"], textarea').each(function () {
        if ($(this).val() == "") {
            $(this).addClass('input-error');
            next_step = false;
        }
        else {
            $(this).removeClass('input-error');
        }
    });

    if (next_step) {
        if (user_exists) {
            return 1;
        }
        parent_fieldset.fadeOut(400, function () {
            $(this).next().fadeIn();
        });
    }
};
jQuery(document).ready(function() {

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", '{{ csrf_token }}');
            }
        }
    });
    /*
        Fullscreen background
    */
   
    
    $('#top-navbar-1').on('shown.bs.collapse', function(){
    	$.backstretch("resize");
    });
    $('#top-navbar-1').on('hidden.bs.collapse', function(){
    	$.backstretch("resize");
    });
    
    /*
        Form
    */
    $('.registration-form fieldset:first-child').fadeIn('slow');
    
    $('.registration-form input[type="text"], .registration-form input[type="password"], .registration-form textarea').on('focus', function() {
    	$(this).removeClass('input-error');
    });
    
    // next step
    $('.registration-form .btn-next1').on('click', function () {
        var parent_fieldset = $(this).parents('fieldset');
        var next_step = true;

        parent_fieldset.find('input[type="text"], input[type="password"], textarea').each(function () {
            if ($(this).val() == "") {
                $(this).addClass('input-error');
                next_step = false;
            }
            else {
                $(this).removeClass('input-error');
            }
        });

        if (next_step) {
            parent_fieldset.fadeOut(400, function () {
                $(this).next().fadeIn();
            });
        }

    });
    

    // previous step
    $('.registration-form .btn-previous').on('click', function() {
    	$(this).parents('fieldset').fadeOut(400, function() {
    		$(this).prev().fadeIn();
    	});
    });
    
    // submit
    $('.registration-form').on('submit', function(e) {
    	
    	$(this).find('input[type="text"], input[type="password"], textarea').each(function() {
    		if( $(this).val() == "" ) {
    			e.preventDefault();
    			$(this).addClass('input-error');
    		}
    		else {
    			$(this).removeClass('input-error');
    		}
    	});
    	
    });
    
    
});
