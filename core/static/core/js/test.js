"use strict";


function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function selectRandom() {
    var questionElements = document.getElementById("questions").children;
    var questions = [];
    for (var i = 0; i < questionElements.length; ++i)
        questions.push(questionElements[i].textContent);

    var randomIndex = getRandomInt(0, questions.length - 1);
    var question = (randomIndex + 1) + ". " + questions[randomIndex];

    var questionTextNode = document.getElementById("questionText");
    questionTextNode.textContent = question;
}
