"use strict";


function randint(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}

function getQuestions() {
    var questions = [];
    $("#questions").children().each(function () {
        questions.push($(this).text());
    });

    return questions;
}

function getIndices() {
    var indicesString = $("#question-range").val();
    if (indicesString === "")
        return null;

    var groups = indicesString.match(/^(\d+)-(\d+)$/);
    if (groups === null) {
        throw {
            name: "InvalidRange",
            message: "Invalid range string!"
        };
    }

    var from = parseInt(groups[1]);
    var to = parseInt(groups[2]);

    return [from, to];
}

$("#next-button").click(function () {
    var questions = getQuestions();
    var from, to;
    try {
        var range = getIndices();
        if (range === null) {
            from = 1;
            to = questions.length;
        } else {
            from = range[0];
            to = range[1];
        }

        if (from < 1 || from > questions.length || to < from || to > questions.length) {
            throw {
                name: "InvalidRange",
                message: "Range out of bounds!"
            }
        }
    } catch (ex) {
        $("#range-error-text").text(ex.message);
        $("#range-error-box").show(100);
        return;
    }
    $("#range-error-box").hide(100);

    var randomIndex = randint(from - 1, to);
    var question = (randomIndex + 1) + ". " + questions[randomIndex];

    $("#question-text").text(question);
});
