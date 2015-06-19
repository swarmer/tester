"use strict";


var questions = null;
var questionsActive = null;
var currentQuestionIndex = null;
var testName = null;
var csrfToken = null;

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

function nextQuestion() {
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
        $("#done-button").prop("disabled", true);
        return;
    }
    $("#done-button").prop("disabled", false);

    var randomIndex = _.sample(validIndices);
    currentQuestionIndex = randomIndex;
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

function postQuestionStates() {
    $.post("/miniapi/questions/save_active/", {
        states: questionsActive,
        test: testName
    });
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


$(document).ready(function () {
    questions = getQuestions();
    questionsActive = fillArray(questions.length, true);
    testName = $("#test-name").text();
    csrfToken = Cookies.get('csrftoken');

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrfToken);
            }
        }
    });

    $("#done-button").click(function () {
        setActive(currentQuestionIndex, false);
        nextQuestion();
        postQuestionStates();
    });

    $("#next-button").click(nextQuestion);

    $("#reset-button").click(function () {
        for (var i = 0; i < questions.length; ++i)
            setActive(i, true);
        postQuestionStates();
    });

    $(".question-link").click(function(event) {
        event.preventDefault();

        var index = $(this).parent().index();
        toggleActive(index);
        $(this).blur();

        postQuestionStates();
    });
});
