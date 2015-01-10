function ajaxOvverideForm($form, $elementToDelete) {
    $form.submit(function (e) {
        e.preventDefault();
        $.ajax({
            type: $form.attr('method'),
            url: $form.attr('action'),
        }).then(function () {
            toastr.success('Успешно изтрихте записа');
            $elementToDelete.remove();
        }, function () {
            toastr.error('Моля опитайте отново');
        });

        e.preventDefault();
    });


    $form.click(function (event) {
        if (!confirm('Сигурни ли сте, че искате да изтриете темата?')) {
            event.preventDefault();
        }
    });
}