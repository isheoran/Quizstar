function loadJson(selector) {
    return JSON.parse(document.querySelector(selector).getAttribute('data-json'));
}

const data = loadJson('#jsonData');
let quizDB = [];

for(let i=0;i<data.length;i++) {
    const miniData = data[i];
    let tmp = {};
    tmp["question"] = "Q"+(quizDB.length+1)+" : "+miniData[0];
    tmp["a"] = miniData[1];
    tmp["b"] = miniData[2];
    tmp["c"] = miniData[3];
    tmp["d"] = miniData[4];
    tmp["ans"] = miniData[5];
    quizDB.push(tmp)
}

const question = document.querySelector('.question')
const option1 = document.querySelector('#op1')
const option2 = document.querySelector('#op2')
const option3 = document.querySelector('#op3')
const option4 = document.querySelector('#op4')
const submit = document.querySelector('#submit')
const answers = document.querySelectorAll('.answer')
const showScore = document.querySelector('#showScore')
const showAnswer = document.querySelector('.anss')
const selectedOption = document.querySelector('.selectedOption')
const optionsList = document.querySelector('.optionslist')

let questionNum = 0;
let myScore = 0;
let checkAnswer = false;

let startedAnswerChecking = false;

let myAnswers = [];

const loadQuestion = () => {
    const question_db = quizDB[(questionNum)%quizDB.length];
    question.innerHTML = question_db.question;
    option1.innerHTML = question_db.a;
    option2.innerHTML = question_db.b;
    option3.innerHTML = question_db.c;
    option4.innerHTML = question_db.d;
    showAnswer.innerHTML = "Answer : " + question_db.ans;

    if(questionNum >= quizDB.length) {
        startedAnswerChecking = true;
        selectedOption.innerHTML = "You selected " + myAnswers[questionNum%quizDB.length];
    }
}

loadQuestion();

const getCheckedAnswer = () => {
    let answer;
    answers.forEach((curAnswer)=> {
        if(curAnswer.checked) {
            answer = curAnswer.id;
        }
    })
    return answer;
}

const deselectAll = () => {
    answers.forEach(curEl => curEl.checked = false)
}

submit.addEventListener(('click'), ()=> {

    if(startedAnswerChecking == false && questionNum>=quizDB.length) {
        questionNum--;
        question.style['display'] = 'flex';
        optionsList.style['display'] = 'flex';
        optionsList.style['flex-direction'] = 'column';
        showScore.style['display'] = 'none';
    }

    const checkedAnswer = getCheckedAnswer();
    if(questionNum<quizDB.length && checkedAnswer == quizDB[questionNum].ans) {
        myScore++;
    }
    if(questionNum<quizDB.length) {
        if(checkedAnswer) myAnswers.push(checkedAnswer);
        else myAnswers.push("None");
    }
    questionNum++;
    deselectAll()
    if(questionNum < quizDB.length-1) {
        loadQuestion();
    }
    else if(questionNum < quizDB.length) {
        loadQuestion();
        submit.innerHTML = "Submit";
    }
    else if(checkAnswer) {
        loadQuestion();
        showAnswer.style['display'] = "flex";
    }
    else {
        
        question.style['display'] = 'none';
        optionsList.style['display'] = 'none';

        submit.innerHTML = "Check Answer"
        showScore.innerHTML = `
            <h2 style='text-align:center'>You Scored ${myScore}/${quizDB.length}</h2>
        `;

        showScore.style['display'] = "flex";
        checkAnswer = true;
    }
})