$(function(){
    setInterval(function() {
        $.getJSON('/lots.json', function (data) {
            data["lots"].forEach(function (lot) {
                $(`#lot-${lot.id}-cars`).text(lot.cars);
                lot.nodes.forEach(function (node) {
                    if (!$(`node-${node.id}`).length) {
                        $(`<p id="node-${node.id}"></p>`).appendTo($(`#lot-${lot.id}-body`));
                    }
                    $(`node-${node.id}`).text(
                        `<b>Node: ${node.id}</b> \
                         <span class="node-in"><i class="glyphicon glyphicon-arrow-up"></i> 0</span> \
                         <span class="node-in"><i class="glyphicon glyphicon-arrow-down"></i> 0</span>`
                    );
                });
            });
        });
    }, 200);
});
