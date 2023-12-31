const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

const swalWithBootstrapButtons = Swal.mixin({
    customClass: {
        confirmButton: "btn btn-success",
        cancelButton: "btn btn-danger"
    },
    buttonsStyling: false
});

$(document).on("click", ".open-Dialog", function () {
    let project_name = $(this).data('project-name')
    let url = $(this).data('url')
    let id = $(this).data('id')
    $(".modal-body").html("Are you sure you want to delete the project: " + project_name)

    $(document).on("click", "#deleteButton", function () {
        $.ajax({
            type: "POST",
            headers: { 'X-CSRFToken': csrftoken },
            url: url,
            data: {},
            success: () => {
                swalWithBootstrapButtons.fire({
                    title: "Deleted!",
                    text: "Your project has been deleted.",
                    icon: "success"
                });
                $(`#${id}`).remove()
            },
            error: () => {
                swalWithBootstrapButtons.fire({
                    title: "Fail",
                    text: "Fail to delete project",
                    icon: "error"
                });
            }
        });
    })
});

