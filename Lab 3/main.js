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
        <div class="task ${item.isdone ? 'done' : ''}">
             <span class="description">${item.description}</span>
             <input onclick="DoneTask(${index})" class="check" type="checkbox" ${item.isdone ? 'checked' : ''}>
             <button onclick="TaskDelete(${index})" class="delete">Delete</button>
        </div>
    `
}

function local(){
    localStorage.setItem('tasks', JSON.stringify(ToDoList));
}

function PushTask(){
    Todos.innerHTML = '';
    if(ToDoList.length > 0){
        ToDoList.forEach((item, index) => {
            Todos.innerHTML += CreateTemp(item, index);
        })
    }
}

function DoneTask(index){
    ToDoList[index].isdone = !ToDoList[index].isdone;
    local();
    PushTask();
}

function TaskDelete(index){
    ToDoList.splice(index, 1);
    local();
    PushTask();
}

AddButton.addEventListener('click', () => {
    ToDoList.push(new CreateTask(TaskInput.value));
    local();
    PushTask();
    TaskInput.value = '';
})

PushTask();