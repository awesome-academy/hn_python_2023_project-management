$(document).ready(function () {
    function remove_member(csrftoken, url, user_id, stage_id) {
        const swalWithBootstrapButtons = Swal.mixin({
            customClass: {
                confirmButton: "btn btn-success",
                cancelButton: "btn btn-danger"
            },
            buttonsStyling: false
        });

        swalWithBootstrapButtons.fire({
            title: "Are you sure?",
            text: "You won't be able to revert this!",
            icon: "warning",
            showCancelButton: true,
            confirmButtonText: "Yes, delete it!",
            cancelButtonText: "No, cancel!",
            reverseButtons: true
        }).then((result) => {
            if (result.isConfirmed) {
                $.ajax({
                    type: "POST",
                    headers: {'X-CSRFToken': csrftoken},
                    url: url,
                    data: {user_id, stage_id},
                    success: (res) => {
                        let remove_id = 'mem-' + user_id

                        $(`#${remove_id}`).remove()
                        swalWithBootstrapButtons.fire({
                            title: "Deleted!",
                            text: "Your stage has been deleted.",
                            icon: "success"
                        });
                    },
                    error: (res) => {
                        swalWithBootstrapButtons.fire({
                            title: "Cancelled",
                            text: res.responseJson.message,
                            icon: "error"
                        });
                    }
                });
            } else if (
                result.dismiss === Swal.DismissReason.cancel
            ) {
                swalWithBootstrapButtons.fire({
                    title: "Cancelled",
                    text: "Your imaginary stage is safe :)",
                    icon: "error"
                });
            }
        });
    }

    $(".remove-member").on("click", function () {
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        let stage_id = $(this).data("stage-id")
        let user_id = $(this).data("user-id")
        let url = $(this).data("url")
        remove_member(csrftoken, url, user_id, stage_id)
    })
})
