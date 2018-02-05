$(document).ready(function() {
            $("#like_button").click(function(event) {
                    event.preventDefault();
                    console.log('ok')

                    $.ajax({
                            'url': '/test/(\d+)',
                        },

                    }); // End of submit event

            }); // End of document ready