$(document).ready(function() {
            $("#like_button").click(function(event) {
                event.preventDefault();
                console.log('ok')

                $.ajax({
                    'url': '/test/(\d+)',
                    'type': 'POST',
                    'data': form.serialize(),
                    'dataType': 'json',
                    'success': function(data) {
                        alert(data['success'])
                    },

                }); // End of submit event

            }); // End of document ready