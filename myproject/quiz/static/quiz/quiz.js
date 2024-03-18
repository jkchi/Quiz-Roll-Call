// fetch data from quiz/<pk>/data 
// and render them in quiz/<pk>

// the current url is quiz/<pk>
const url = window.location.href

// the locaiton of the quiz content is define by #quiz-box
const quizBox = document.querySelector('#quiz-box')
const scoreBox = document.querySelector('#score-box')
const resultBox = document.getElementById('result-box')
const submitBtn = document.querySelector('button[type="submit"].btn.btn-primary');

const renderQuiz = async () => {
    const response = await fetch(`${url}/data`);
    const json = await response.json();
    const data = json.data;
    const time = json.time;

    data.forEach(element => { 
        
        // Object.entries is use to get the key value pair of question and answer 
        // question: str key
        // answer:array[str]


        for (const [question, answers] of Object.entries(element)){

            quizBox.innerHTML  += `
                <hr>
                <div class="mb-2">
                    <b>${question}</b>
                </div>
            `
            answers.forEach(answer=>{
                // as defined above the value of each quesion is the choice and name is the question text
                quizBox.innerHTML += `
                    <div>
                        <input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}">
                        <label for="${question}">${answer}</label>
                    </div>
                `
            })
        }
    })
    
    
};


renderQuiz()


// get the result of the form
const quizForm = document.getElementById('quiz-form')
// get the csrf token
const csrf = document.getElementsByName('csrfmiddlewaretoken') 

const checkResult = () => {
    
    // get all the elements with class .ans
    const elements = document.querySelectorAll('.ans')
    const data = {}

    elements.forEach(e => {
        if (e.checked) {
            // if a choice is choosed assign the questions and answer pair
            data[e.name] = e.value
        } else {
            if (!data[e.name]){
                data[e.name] = null
            }
        }
    })

    fetch(`${url}/save`, { 
    method: 'POST', 
    headers: {
        // include header
        'Content-Type': 'application/json', 
        // the key of csrf is X-CSRFToken
        "X-CSRFToken":csrf[0].value
    },
    body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json()})
        .then(json => {
            const results = json.results
            const n_correct_answers = json.correct_questions
            const score = json.score

            // clear the form the form 
            quizForm.remove()

            let scoreDiv = document.createElement('div')
            
            scoreDiv.innerHTML = `
                               <p> Your result is ${score} %</p>
                               <p> Answered correctly: ${n_correct_answers}</p>
                               `
            scoreBox.append(scoreDiv)

            results.forEach(res =>{
                let resDiv = document.createElement('div')
                for (const [question, resp] of Object.entries(res)){
                    resDiv.innerHTML += question

                    const classes = ['container', 'p-3', 'text-light', 'h4']
                    resDiv.classList.add(...classes)

                    if (resp == 'not answered'){
                        resDiv.innerHTML += ' — Not answered'
                        resDiv.classList.add('bg-danger')
                    } else{
                        const answer = resp['answered']
                        const correct = resp['correct_answer']

                        if (answer == correct){
                            resDiv.classList.add('bg-success')
                            resDiv.innerHTML += ` Answered: ${answer}`
                        } else {
                            resDiv.classList.add('bg-danger')
                            resDiv.innerHTML += `| Answered: ${answer}`
                            resDiv.innerHTML += `| Correct answer: ${correct}`
                        }
                    }
                }
                resultBox.append(resDiv)
                
            })
            const quizExtBtn = document.querySelector("#quiz-back-button")
            quizExtBtn.hidden = false
        })
    }


submitBtn.addEventListener('click', () => {
    submitBtn.disabled = true
    checkResult()
})


