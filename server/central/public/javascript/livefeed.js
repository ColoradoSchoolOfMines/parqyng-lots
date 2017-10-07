$(function(){
    function status(lot) {
        var percent = lot.cars / lot.capacity;
        if (percent < 0.9) return 'success';
        if (percent < 0.95) return 'warning';
        return 'danger';
    };

    var prev_lot_counts = [];
    var prev_in_and_out = [];
    var show_counters = [];

    setInterval(function() {
        $.getJSON('/lots.json', function (data) {
            data["lots"].forEach(function (lot, i) {
                var in_and_out = `<span class="node-stable"> \
                    <i class="glyphicon glyphicon-minus"></i> 0 \
                </span>`

                if (prev_lot_counts != 0) {
                    if (lot.cars > prev_lot_counts[i]) {
                        in_and_out = `<span class="node-in"> \
                            <i class="glyphicon glyphicon-arrow-up"></i> ${lot.cars - prev_lot_counts[i]} \
                        </span>`;
                    } else if (lot.cars < prev_lot_counts[i]) {
                        in_and_out =  `<span class="node-out"> \
                            <i class="glyphicon glyphicon-arrow-down"></i> ${prev_lot_counts[i] - lot.cars} \
                        </span>`;
                    }
                }

                $(`#lot-${lot.id}-cars`).html(lot.cars + ` (${in_and_out})`);
                lot.nodes.forEach(function (node) {
                    if (!$(`#node-${node.key}`).length) {
                        $(`<p id="node-${node.key}"></p>`).appendTo($(`#lot-${lot.id}-body`));
                    }
                    $(`#node-${node.key}`).html(`<b>Node: ${node.key}</b>`);
                });
                $(`#lot-${lot.id}`).removeClass("panel-success panel-warning panel-danger").addClass(`panel-${status(lot)}`);
            });

            prev_lot_counts = data['lots'].map(l => l.cars)
        });
    }, 2000);
});
