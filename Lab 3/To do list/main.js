const AddButton = document.getElementById('add-button');
const TaskInput = document.getElementById('task-description');
const Todos = document.getElementById('todos');

let ToDoList;
localStorage.tasks ? ToDoList = JSON.parse(localStorage.getItem('tasks')) : ToDoList = [];

function CreateTask(description){
    this.description = description;
    this.isdone = false;
}

function CreateTemp(item, index){
    return `
        <div class="task">
             <span class="description">ASDSDasdasd</span>
             <input class="check" type="checkbox">
             <button class="delete">Delete</button>
        </div>
    `

}

function local(){
    localStorage.setItem('tasks', JSON.stringify(ToDoList));
}


AddButton.addEventListener('click', () => {
    ToDoList.push(new CreateTask(TaskInput.value));
    local();
    console.log(ToDoList);
})

function AddTask(){
    Todos.innerHTML = '';
    if(ToDoList.length > 0){
        ToDoList.forEach((item, index) => {
            Todos.innerHTML += CreateTemp(item, index);
        })
    }
}