$(function(){
    function status(lot) {
        var percent = lot.cars / lot.capacity;
        if (percent < 0.9) return 'success';
        if (percent < 0.95) return 'warning';
        return 'danger';
    };
    setInterval(function() {
        $.getJSON('/lots.json', function (data) {
            data["lots"].forEach(function (lot) {
                $(`#lot-${lot.id}-cars`).text(lot.cars);
                lot.nodes.forEach(function (node) {
                    if (!$(`#node-${node.key}`).length) {
                        $(`<p id="node-${node.key}"></p>`).appendTo($(`#lot-${lot.id}-body`));
                    }
                    $(`#node-${node.key}`).html(
                        `<b>Node: ${node.key}:</b> \
                         <span class="node-in"><i class="glyphicon glyphicon-arrow-up"></i> 0</span> \
                         <span class="node-in"><i class="glyphicon glyphicon-arrow-down"></i> 0</span>`
                    );
                });
                $(`#lot-${lot.id}`).removeClass("panel-success panel-warning panel-danger").addClass(`panel-${status(lot)}`);
            });
        });
    }, 200);
});
