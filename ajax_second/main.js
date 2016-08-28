
function get_items() {
    function success(json) {
        items = json.data;
        div_items = $('#items');
        ul = $('<ul/>');
        $.each(items, function (i, item) {
            li = $('<li/>').text(item.name + " " + item.bonus + " " + item.modif).appendTo(ul)
        });
        ul.appendTo(div_items);
        $('#p1').html(items[0].name);
    };

    $.ajax({
        url: 'http://192.168.0.103:8000/api_get_items/',
        //url: 'data.json',
        success: success,
        dataType: 'json'
    })
}


function get_players() {
    function success(json) {
        players = json.data;
        function set_select_players(select, players) {
            $.each(players, function (i, player) {
                option = $('<option/>').text(player.name).attr({value: player.id});
                select.append(option);
            });
        }
        set_select_players($('#select_fit3'), players);
        set_select_players($('#select_power1'), players);
        set_select_players($('#select_power2'), players);
        set_select_players($('#select_power3'), players);
    };

    $.ajax({
        //url: 'http://192.168.0.103:8000/api_get_players/',
        url: 'players.json',
        success: success,
        dataType: 'json'
    })
}

// {"intel": 10, "hp": 100, "weapon": 5, "id": 1, "name": "dan", "status": 1, "strength": 10, "mp": 100, "dmg": 10, "dex": 10, "game": 1}
function get_player() {
    function success(json) {
        player = json;
        console.log(player);
        $('#stren').html(player.strength)
        $('#hp').html(player.hp)
        $('#intel').html(player.intel)
        $('#mp').html(player.mp)
        $('#dex').html(player.dex)

    };

    $.ajax({
        url: 'http://192.168.0.103:8000/api_get_player/1',
        //url: 'data.json',
        success: success,
        dataType: 'json'
    })
}

$(document).ready(function () {
    get_items();
    get_players();
    //var charname = prompt('charname', "");
    //$('#ch').html(charname);

    get_player();
    setInterval(get_player, 5000);


    function fitClick(e) {
        button_id = e.currentTarget.id
        data = {};
        data['button'] = button_id;
        data['target'] = $('#select_'+button_id).val();
        data['id'] =1 ;
        $.ajax({
            type: "POST",
            url: 'http://127.0.0.1:8000/api_user_command/1',
            data: data,
            success: success,
            dataType: 'json'
        })
    }
    $('#fit1').click(fitClick);
    $('#fit2').click(fitClick);
    $('#fit3').click(fitClick);
    $('#power1').click(fitClick);
    $('#power2').click(fitClick);
    $('#power3').click(fitClick);

});