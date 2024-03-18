// get all model botton(quiz obj)
const modalButtons = document.querySelectorAll(".modal-button");

const modalBody = document.querySelector('#modal-body-confirm')

const startButton = document.querySelector('#startButton')

// get the current url
const url = window.location.href

// define the current activate quiz pk
// the variable will be used by the event listener added to the startButton
let activeQuizPK = ''; 


// iter the all the quiz Button
// add the click event listener 
// and apply the html attr to modal
// these html attr is passed in by django
modalButtons.forEach(Button => Button.addEventListener('click', ()=>{
    const pk = Button.getAttribute('data-pk')
    const date = Button.getAttribute('data-date')
    const name = Button.getAttribute('data-name')
    const description = Button.getAttribute('data-description')
    const numQuestions = Button.getAttribute('data-questions')
    const time = Button.getAttribute('data-time')

    activeQuizPK = pk

    // inject the html to the only modal body and change the text on the modal
    modalBody.innerHTML = `
        <div class="mb-3">
            <h5>Are you sure you want to begin "<b>${name}</b>"</h5>
        </div>
        
        <div class="text-muted">
            <p>${description}</p>
            <ul>
                <li>Created at: <b>${date}</b></li>
                <li>Number of questions: <b>${numQuestions}</b></li>
                <li>Time available: <b>${time} minutes</b></li>
            </ul> 
        </div>
    
    `
}))


// add the event listener once and the effect will be change be use the var activeQuizPK
startButton.addEventListener('click', () => {
    if (activeQuizPK) {
        window.location.href = `${url}${activeQuizPK}`; // Takes the user to the detail view
    }
});