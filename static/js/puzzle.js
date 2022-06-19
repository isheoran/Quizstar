function loadJson(selector) {
    return JSON.parse(document.querySelector(selector).getAttribute('data-json'));
}

const data = loadJson('#jsonData');

const Puzzle = {
    title : data[0],
    statement : data[1],
    ans : data[2]
}

const title = document.querySelector('.title');
const question = document.querySelector('.question');
const answer = document.getElementById('answer');
const submit = document.getElementById('submit');
const sttatus = document.querySelector('.status');


const load_question =()=> {
    title.innerHTML = Puzzle.title;
    question.innerHTML = Puzzle.statement;
    answer.value = "";
}

load_question()

let flag = 0;

submit.addEventListener(('click'), ()=> {

    if(flag == 2) {
        window.location.reload();
    }

    if(flag == 1) {
        sttatus.innerHTML = "Correct Answer is " + Puzzle.ans;
        sttatus.style['color'] = 'black';
        flag = 2;

        submit.innerHTML = "Next Puzzle";
    }
    else {
        user_ans = answer.value;
        if(user_ans) {
            if(Puzzle.ans == user_ans) {
                sttatus.innerHTML = "Correct Answer";
                sttatus.style['color'] = 'green';
            }
            else {
                sttatus.innerHTML = "Incorrect Answer";
                sttatus.style['color'] = 'red';
            }
    
            flag = 1;

            submit.innerHTML = "Check Answer";
        }
    }
})