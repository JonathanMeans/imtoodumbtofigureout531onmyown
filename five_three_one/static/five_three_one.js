var mark_first_set_as_current_set = function() {
    const first_row = $("#id_workout_table tbody tr:first");
    first_row.addClass("current-set");
}

var advance_current_set = function() {
    const first_row = $("#id_workout_table tbody .current-set");
    first_row.removeClass("current-set")

    // const second_row = $("#id_workout_table tbody tr:nth-child(2)");
    const second_row = first_row.next();
    second_row.addClass("current-set");
}

var five_three_one_initialize = function() {
    mark_first_set_as_current_set();

    $("#id_next_set").on("click", advance_current_set)
}