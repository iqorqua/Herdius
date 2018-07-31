$(function () {

        $("#fileinfo").validate({

            rules: {

                username: {
                    required: true,
                    minlength: 4,
                    maxlength: 16,
                },

                first_name: {
                        required: true,
                        minlength: 6,
                        maxlength: 16,
                    },
                },

        });

        $("#btn_names").click(function () {
            $("#fileinfo").validate().element("#username");
        });
});