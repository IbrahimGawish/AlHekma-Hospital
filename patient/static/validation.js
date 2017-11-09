
$(document).ready(function () {



            $('#patientform').validate({
           // alert("hello");
             rules: {
                name: {
                    minlength: 2,
                    required: true
                     },

                phyiscian: {
                    minlength: 2,
                    required: true
                },
                diagonistics:{
                    required : true
                },
                image:{
                    required: true,
                    //extension: "xls|csv"
                }
             },
            highlight: function (element) {
                $(element).closest('.control-group').removeClass('success').addClass('error');
            },
            success: function (element) {
                element.text('OK!').addClass('valid')
                .closest('.control-group').removeClass('error').addClass('success');
            }
            });


            });

