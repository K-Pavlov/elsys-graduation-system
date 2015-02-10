/// <reference path="../libs/jquery-1.10.2.js" />
$(document).ready(function () {
    var $button = $('#send-button');
    $button.click(function () {
        markData();
        getData();
    });

    function markData() {
        var $selects = $('.choosen-data-type');
        $selects.each(function () {
            var $this = $(this);
            //console.log($this.val());
            var $dataForType = $('.' + $this.attr('id').replace('select-', ''));
            $dataForType.each(function () {
                var $self = $(this);
                $self.attr('type', $this.val());
            });
        });
    }

    function getData() {
        var $dataRows = $('.row-data'),
            dataObjects = [];

        $dataRows.each(function () {
            var $this = $(this),
                $data = $this.children('td'),
                cleanData = {};

            $data.each(function () {
                var $self = $(this),
                    type = $self.attr('type');
                if (type) {
                    cleanData[type] = $self.html().trim();
                }
            });
            dataObjects.push(cleanData);
        });

        $.each(dataObjects, function () {
            console.log(this);
        });
    }
});