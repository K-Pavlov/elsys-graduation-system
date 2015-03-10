$(document).ready(function () {
    function addPageActions() {
        var $prevPage = $('#previous-page'),
            $nextPage = $('#next-page'),
            $firstPage = $('#first-page'),
            $lastPage = $('#last-page'),
            $pageLinks = $('.page-link');

        addClick($firstPage);
        addClick($prevPage);
        $pageLinks.each(function () {
            var $this = $(this);
            addClick($this);
        });

        addClick($nextPage);
        addClick($lastPage);
    }

    function addClick($target) {
        var $replaceDiv = $('#table-replace'),
            viewName = $('#create-link').attr('href').split('/')[1];

        $target.click(function () {
            $.get('/' + viewName + '/page/' + $target.attr('page-number') + '/')
                .then(function (data) {
                    $replaceDiv.html(data);
                    makeSortable();
                    addPageActions();
                    addDeletation();
                });
        });
    }

    function makeSortable() {
        var th = $('#all-table th').not('.ignore'),
        inverse = false;

        th.click(function () {
            var header = $(this),
                index = header.index();

            $('#all-table').find('td')
                .filter(function () {
                    return $(this).index() === index;
                })
                .sort(function (a, b) {
                    a = $(a).text();
                    b = $(b).text();
                    return (isNaN(a) || isNaN(b) ? a > b : +a > +b) ? (inverse ? -1 : 1) : (inverse ? 1 : -1);
                }, function () {
                    return this.parentNode;
                });

            inverse = !inverse;
        });
    }

    function addDeletation() {
        var $form = $('.delete-form');
        $form.each(function () {
            var $this = $(this),
                $objectToDelete = $('#' + $this.attr('object-id'));

            ajaxOvverideDelForm($this, $objectToDelete);
        });
    }

    addPageActions();
    makeSortable();
    addDeletation();
});