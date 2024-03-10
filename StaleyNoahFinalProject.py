from breezypythongui import EasyFrame
from datetime import datetime
from tkcalendar import Calendar
from tkinter import END

class TodoList(EasyFrame):
    def __init__(self):
        #Sets up the window and the widgets.
        EasyFrame.__init__(self, title="Procrastination Solver")

        # Label for task
        self.addLabel(text="Enter task:", row=0, column=0)

        # Text field to enter tasks
        self.taskField = self.addTextField(text="", row=0, column=1)

        # Label for due date
        self.addLabel(text="Due Date:", row=1, column=0)

        # Button to open date picker
        self.addButton(text="Select Date", row=1, column=1, command=self.showDatePicker)
     
        # List box to display tasks with due dates
        self.taskList = self.addListbox(row=2, column=0, columnspan=3)

        # Button to mark task as completed and so on
        self.addButton(text="Mark Completed", row=3, column=0, command=self.markCompleted)
        self.addButton(text="Delete Task", row=3, column=1, command=self.deleteTask)
        self.addButton(text="Clear All", row=3, column=2, command=self.clearAll)
        self.addButton(text="Submit", row=0, column=2, command=self.addTask)

        # Dictionary to store tasks and their due dates
        self.tasks = {}

    def addTask(self):
        #Adds a new task to the list.
        task = self.taskField.getText()
        if task != "":
            due_date = datetime.now().strftime("%Y-%m-%d")
            self.addTaskToList(task, due_date)
            self.taskField.setText("")

    def addTaskToList(self, task, due_date=None):
        #Adds a task to the list.
        if due_date:
            task_with_date = f"{task} (Due: {due_date})"
            self.taskList.insert(END, task_with_date)
            self.tasks[task_with_date] = due_date
        else:
            self.taskList.insert(END, task)
            self.tasks[task] = None

    def showDatePicker(self):
        #Opens a date picker in a separate window for selecting due dates.
        # Create a new EasyFrame window for the date picker
        date_picker_window = EasyFrame(title="Select Due Date", width=300, height=500)

        # Create a Calendar widget
        calendar = Calendar(date_picker_window)
        calendar.pack(fill="both", expand=True)

        def setDueDate():
            # Get the selected date from the calendar widget
            selected_date = calendar.get_date()
            # Add the selected date to the task list
            
            self.addTaskToList(self.taskField.getText(), selected_date)
            # Close the date picker window
            date_picker_window.destroy()

        # Add a button to confirm the selected date
        select_button = self.addButton(text="Confirm Date", row=1, column=2, command=self.showDatePicker)
        select_button["command"] = setDueDate  # Assign the command to the button

        # Run the date picker window loop
        date_picker_window.mainloop()

    
    def markCompleted(self):
        #Marks task as completed.
        selected_index = self.taskList.getSelectedIndex()
        if selected_index != -1:
            task = self.taskList.get(selected_index)
            del self.tasks[task]
            self.taskList.delete(selected_index)

    def deleteTask(self):
        #Deletes task.
        selected_index = self.taskList.getSelectedIndex()
        if selected_index != -1:
            task = self.taskList.get(selected_index)
            del self.tasks[task]
            self.taskList.delete(selected_index)

    def clearAll(self):
        #Clears all tasks from the list.
        self.tasks.clear()
        self.taskList.clear()

def main():
    TodoList().mainloop()

if __name__ == "__main__":
    main()
