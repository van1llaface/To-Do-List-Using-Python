import streamlit as st

# create an empty list to store tasks
tasks = []

# define a function to add tasks
def add_tasks(new_tasks):
    for task in new_tasks:
        tasks.append(task)


# define the main function
def main():
    # set the page title
    st.title("To-Do List App")
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    # create a textarea input to enter new tasks
    new_tasks = st.text_area("Enter new tasks, one per line:")

    # add the new tasks when the "Add" button is clicked
    if st.button("Add"):
        add_tasks(new_tasks.split("\n"))

    # display the list of tasks
    if tasks:
        st.write("### Tasks:")
        for i, task in enumerate(tasks):
            st.write(f"{i+1}. {task}")
    else:
        st.write("No tasks added yet.")

if __name__ == "__main__":
    main()
