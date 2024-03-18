// fetch data from quiz/<pk>/data 
// and render them in quiz/<pk>

// the current url is quiz/<pk>
const url = window.location.href

// the locaiton of the quiz content is define by #quiz-box
const quizBox = document.querySelector('#quiz-box')

const getData = async () => {
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

getData()