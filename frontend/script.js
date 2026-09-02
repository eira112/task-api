const API_URL = "/api";

const taskList = document.getElementById("task-list");
const taskTitle = document.getElementById("task-title");
const addButton = document.getElementById("add-task");
const errorMsg = document.getElementById("error-message");

addButton.addEventListener("click", async () => {

    const title = taskTitle.value;

    if (title.trim() === "") {
        errorMsg.textContent = "Task title cannot be empty";
        return;
    }

    const request = await fetch(`${API_URL}/tasks`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({title: title})
    });

    if (request.ok) {
        await loadTasks();

        taskTitle.value = "";
        errorMsg.textContent = "";
    }

});

async function loadTasks() {

    const response = await fetch(`${API_URL}/tasks`);
    const tasks = await response.json();

    taskList.innerHTML = "";

    tasks.forEach((task) => {

        const taskElement = document.createElement("div");

        taskElement.classList.add("task");

        taskElement.innerHTML = `
            <span>
                <input 
                    type="checkbox" 
                    class="completed-checkbox" 
                    data-id="${task.id}"
                    ${task.completed ? "checked" : ""}
                >
                <label>${task.title}</label>
            </span>
            <button class="delete-btn" data-id="${task.id}">Delete</button>
        `;

        taskList.appendChild(taskElement);

        const checkbox = taskElement.querySelector(".completed-checkbox");

        checkbox.addEventListener("change", async() => {
            const taskId = checkbox.dataset.id;
            const request= await fetch(`${API_URL}/tasks/${taskId}`,{
                method: "PUT",
                headers: {"Content-Type":"application/json"},
            });
            if(request.ok){
                await loadTasks();
            }


        });

        const deleteBtn=taskElement.querySelector(".delete-btn");
        deleteBtn.addEventListener("click",async()=>{
            const taskId=deleteBtn.dataset.id;
            const request=await fetch(`${API_URL}/tasks/${taskId}`,{
                method:"DELETE",
            });
            if(request.ok){
                await loadTasks();
            }
        });

    });

}

loadTasks();