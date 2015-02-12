/// <reference path="../libs/jquery-1.10.2.js" />
$(document).ready(function () {
    var $button = $('#send-button');
    $button.click(function () {
        markData();
        sendData();
    });

    var $selects = $('.choosen-data-type');
    $selects.each(function () {
        var $this = $(this),
            previous;

        $this.focus(function () {
            previous = $(this).children(':selected');
        }).change(function () {
            var selectValue = $this.val(),
                $selectsToRemove;

            $selectsToRemove = $($.grep($('.choosen-data-type'), function (item) {
                var $item = $(item);
                if ($item.val() === selectValue) {
                    return false;
                }
                return true;
            }));

            $selectsToRemove.each(function () {
                var $self = $(this),
                    $itemToDetach;

                $self.children().each(function () {
                    var $this = $(this);
                    if ($this.val() === selectValue) {
                        $this.detach();
                        return;
                    }
                });

                //console.log($self);
                //if (!$.contains($self, previous)) {
                //    $self.append(previous);
                //}
            });

            previous = $this.children(':selected');
        });
    });

    function markData() {
        var $selects = $('.choosen-data-type');
        $selects.each(function () {
            var $this = $(this);
            var $dataForType = $('.' + $this.attr('id').replace('select-', ''));
            $dataForType.each(function () {
                var $self = $(this);
                $self.attr('type', $this.val());
            });
        });
    }

    function sendData() {
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

        var json = JSON.stringify(dataObjects);
        $.post('/' + $('#send-button').attr('view-name') + '/upload/', json).then(function (data) {
            toastr.success('Успешно създадохте записите');
        }, function (err) {

        });
        console.log(json);
        //$.each(dataObjects, function () {
        //    console.log(this);
        //});
    }
});