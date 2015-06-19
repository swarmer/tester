"use strict";


var questions = null;
var questionsActive = null;

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

function getValidIndices(start, end) {
    var validIndices = [];
    for (var i = 0; i < questions.length; ++i) {
        if (i >= start && i < end && questionsActive[i])
            validIndices.push(i);
    }

    return validIndices;
}

function nextClicked() {
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

    $("#question-text").empty();

    var validIndices = getValidIndices(from - 1, to);
    if (_.isEmpty(validIndices)) {
        $("#question-text").append(
            $("<span/>", {class: "text-success", text: "No more questions!"})
        );
        return;
    }

    var randomIndex = _.sample(validIndices);
    var question = (randomIndex + 1) + ". " + questions[randomIndex];

    $("#question-text").text(question);
}

function fillArray(n, value) {
    var array = new Array(n);
    for (var i = 0; i < n; ++i)
        array[i] = value;
    return array;
}

function setActive(index, isActive) {
    questionsActive[index] = isActive;

    var questionText = $("#questions").children().eq(index).children("a");
    if (isActive) {
        questionText.removeClass("text-success");
        questionText.removeClass("question-inactive");
    } else {
        questionText.addClass("text-success");
        questionText.addClass("question-inactive");
    }
}

function toggleActive(index) {
    setActive(index, !questionsActive[index]);
}


$(document).ready(function () {
    questions = getQuestions();
    questionsActive = fillArray(questions.length, true);

    $("#next-button").click(nextClicked);

    $(".question-link").click(function(event) {
        event.preventDefault();

        var index = $(this).parent().index();
        toggleActive(index);
        $(this).blur();
    });
});
